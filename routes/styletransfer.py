import os, sys
print(sys.path)
from fastapi import APIRouter, File, UploadFile, Header, Depends
from fastapi import BackgroundTasks
# from typing import List, Optional
from routes.styletransfer_depends import params_styletransfer
from controllers.styletransfer import*
from config import config

mycontroller = media_styletransfer(config)

test_config = dict(
    PATH_DATA = "./temp"
)


handler = MediaHandler.Router(mycontroller, MediaHandler.Config(**test_config))
router = APIRouter(prefix="")

@router.post('/transfer-image/')
async def transfer_image(file: UploadFile = File(...), \
                   bgtask: BackgroundTasks = BackgroundTasks(), \
                   params: dict = Depends(params_styletransfer)
                   ):
    """
    Post an image(.jpg ) to make it artistic-style. 
    You can get the artistic-style image using GET /image API. 
    """
    
    # return await handler.post_file("transfer-image", file, "jpg", bgtask, **params)
    return await handler.post_file_BytesIO("transfer-image", file, "jpg", bgtask, **params)
