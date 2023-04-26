# import os, sys
import mediarouter
from fastapi import APIRouter, File, UploadFile, Depends
from fastapi import BackgroundTasks
# from typing import List, Optional
from src.routes_depends import params_styletransfer
from src.styletransfer import media_styletransfer
from src.config import config_org

mycontroller = media_styletransfer(config_org)

test_config = dict(
    PATH_DATA = "./temp"
)


handler = mediarouter.router(
    mycontroller, 
    mediarouter.config(**test_config)
)
router = APIRouter(prefix="")


@router.post('/transferred-image')
async def transferred_image(
    file: UploadFile = File(...),
    bgtask: BackgroundTasks = BackgroundTasks(),
    params: dict = Depends(params_styletransfer)
):
    """
    Post an image(.jpg ) to make it artistic-style. 
    You can get the artistic-style image using GET /image API. 
    """
    
    # return await handler.post_file("transfer-image", file, "jpg", bgtask, **params)
    return await handler.post_file_BytesIO("transferred-image", file, bgtask, **params)
    # return await handler.post_file_BytesIO("transfer-image", file, **params)
