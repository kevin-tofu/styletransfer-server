from mediaBase.controllers.media_base import media_prod
import numpy as np
import onnxruntime as ort

from albumentations import Compose
from albumentations.augmentations.transforms import Normalize
from albumentations.augmentations.geometric.resize import Resize
from skimage import io

import MediaHandler


class media_styletransfer(MediaHandler.Processor):

    def __init__(self, _config):
        super().__init__(**_config)

        #
        # setting
        #
        path_models = _config["PATH_MODEL"]
        
        resize_to2 = (512, 512)
        #print(image_height, image_width)#, w2h_ratio=0.75
        self.transformer = Compose([Resize(resize_to2[0], resize_to2[1], always_apply=True),\
                                    Normalize(always_apply=True)])
        # self.mean = [0.485, 0.456, 0.406]
        # self.std = [0.229, 0.224, 0.225]
        # mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225), max_pixel_value=255.0

        #
        # session
        #
        self.ort_session = ort.InferenceSession(path_models)
        self.ort_session.get_modelmeta()


    async def main_file(self, \
                        process_name: str, \
                        fpath_org: str, \
                        fpath_dst: str, \
                        **kwargs
    ) -> dict:
        
        if process_name == "transfer-image":

            self.transfer(fpath_org, fpath_dst, **kwargs)

            return dict(status = "OK")


    def transfer(self, fpath: str, fpath_ex: str, **kwargs):
        
        image = io.imread(fpath)
        height, width = image.shape[0], image.shape[1]
        # if 'style1' in kwargs.keys():
        style_num = np.array(kwargs['style1']).astype(np.int64)
        style_num2 = np.array(kwargs['style2']).astype(np.int64)
        alpha = np.array(kwargs['alpha']).astype(np.float32)
        image_aug = self.transformer(image=image)['image']
        image_aug = np.expand_dims(image_aug, axis=0).astype(np.float32)

        outputs = self.ort_session.run(
            ["res_img"],
            {"img": image_aug, 
            "style_num": style_num, 
            "style_num2": style_num2, 
            "alpha": alpha}
        )
        
        trans_back = Compose([Resize(height, width, always_apply=True)])
        pred = outputs[0][0]
        pred = trans_back(image=pred)['image']
        # pred = np.transpose(pred, (2, 0, 1))
        # print(pred.shape, type(pred))
        
        io.imsave(fpath_ex, pred)

    