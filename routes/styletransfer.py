import os, sys
print(sys.path)

from fastapi import APIRouter, Request, File, UploadFile, File, Header
from typing import List, Optional
from pydantic import Required

from pydantic import BaseModel
class User(BaseModel):
    user_name: str


from controllers.styletransfer import*
mycontroller = media_styletransfer()


router = APIRouter(prefix="")

@router.post('/image/')
async def post_image(file: UploadFile = File(...), \
                     style1: Optional[int] = 1, \
                     style2: Optional[int] = 2, \
                     alpha: Optional[float] = 0.0, \
                     test: Optional[int] = None):
    """
    Post an image(.jpg ) to make it artistic-style. 
    You can get the artistic-style image using GET /image API. 
    """
    # print(header)
    return await mycontroller.post_image_(file, 
                                          style1=style2, 
                                          style2=style1, 
                                          alpha=alpha, 
                                          test=test)
@router.get('/image/')
def get_image(
              idData: Optional[str] = Header(None), \
            #   id_data: str = Header(Required),
            #   id_data: Optional[str] = None, \
              test: Optional[int] = None):
    """
    Get an artistic-style image. 
    You should set id_data that is gotten from post-API.
    """
    return mycontroller.get_image_(idData, test=test)


# @router.post('/video/')
# async def post_video(file: UploadFile = File(...), \
#                      test: Optional[int] = None):
#     """
#     Post a video(.mp4 ) to draw skeleton on the video. 
#     You can get the video using GET /skeleton_video API. 
#     """
#     return await mycontroller.post_video_(file, test=test)


# @router.get('/video/')
# def get_video(id_data: Optional[str] = None, \
#               test: Optional[int] = None):
#     """
#     Get a video with skeleton. 
#     You should set original file name with API.
#     """
    
#     return mycontroller.get_video_(id_data, test=test)