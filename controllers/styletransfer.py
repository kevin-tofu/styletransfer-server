from mediaBase.controllers.media_base import media_base
import numpy as np
import onnxruntime as ort

from albumentations import Compose
from albumentations.augmentations.transforms import Normalize
from albumentations.augmentations.geometric.resize import Resize
from skimage import io

class media_styletransfer(media_base):

    def __init__(self):
        super().__init__()
        # img = io.imread("./yolo/trump.jpg")
        # data = np.random.randn(480, 640, 3).astype(np.float32)
        #
        # setting
        #
        path_models = './model/result/model.onnx'
        
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
        # first_input_name = self.rt_session.get_inputs()[0]
        # first_output_name = self.ort_session.get_outputs()[0]
        
        # data_aug = np.expand_dims(data_aug, axis=0)


    def draw_info2image(self, image, fpath_ex, **kwargs):
        
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

    
    def draw_info2video(self, fpath_org, fpath_ex, **kwargs):
        pass
    
    def get_info_image(self, image, **kwargs):
        return {}

    def get_info_video(self, fpath_org, **kwargs):
        return {}