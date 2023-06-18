from typing import Optional
import numpy as np
import onnxruntime as ort

from albumentations import Compose
from albumentations.augmentations.transforms import Normalize
from albumentations.augmentations.geometric.resize import Resize
# from skimage import io
import cv2
from PIL import Image
from fastapi import Response
import io
from fastapi import BackgroundTasks

import mediarouter


class media_styletransfer(mediarouter.processor):

    def __init__(self, _config):
        super().__init__()
        
        #
        # setting
        #
        path_models = _config.path_model
        resize_to2 = (_config.imsize_h, _config.imsize_w)
        #print(image_height, image_width)#, w2h_ratio=0.75
        self.transformer = Compose(
            [
                Resize(resize_to2[0], resize_to2[1], always_apply=True),
                Normalize(always_apply=True)
            ]
        )
        # self.mean = [0.485, 0.456, 0.406]
        # self.std = [0.229, 0.224, 0.225]
        # mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225), max_pixel_value=255.0

        #
        # session
        #
        self.ort_session = ort.InferenceSession(path_models)
        self.ort_session.get_modelmeta()

    
    async def post_file_process(
        self,
        process_name: str,
        data: dict,
        file_dst_path: Optional[str] = None,
        bgtask: BackgroundTasks=BackgroundTasks(),
        **kwargs
    ):
        
        if process_name == "transferred-image":
            bytesio = data['file']['bytesio']
            img_pil = Image.open(bytesio)
            img_np = np.asarray(img_pil)
            pred = self.transfer(img_np, **kwargs)
            pred = cv2.cvtColor(pred, cv2.COLOR_RGB2BGR)

            ext = 'jpg'
            _, pred = cv2.imencode(f'.{ext}', pred)

            return Response(
                content = pred.tostring(),
                media_type = f'image/{ext}'
            )
        else:
            raise ValueError('process_name is not set correctly')


    def transfer(
        self, image: np.ndarray, **kwargs
    ):
        
        height, width = image.shape[0], image.shape[1]
        style_num = np.array(kwargs['style1']).astype(np.int64)
        style_num2 = np.array(kwargs['style2']).astype(np.int64)
        alpha = np.array(kwargs['alpha']).astype(np.float32)
        image_aug = self.transformer(image=image)['image']
        image_aug = np.expand_dims(image_aug, axis=0).astype(np.float32)

        outputs = self.ort_session.run(
            ["res_img"],
            {
                "img": image_aug, 
                "style_num": style_num, 
                "style_num2": style_num2, 
                "alpha": alpha
            }
        )
        
        trans_back = Compose([Resize(height, width, always_apply=True)])
        pred = outputs[0][0]
        pred = trans_back(image=pred)['image']
        
        return pred
