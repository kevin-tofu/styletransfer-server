# import os, sys
import filerouter
from fastapi import APIRouter, File, UploadFile, Depends
from fastapi import BackgroundTasks
from src.routes_depends import params_styletransfer
from src.styletransfer import media_styletransfer
from src.config import config_org

mycontroller = media_styletransfer(config_org)

test_config = dict(
    DATA_PATH = "./temp"
)


handler = filerouter.router(
    mycontroller, 
    filerouter.config(**test_config)
)
router = APIRouter(prefix="")


@router.post('/transferred-image')
async def transferred_image(
    file: UploadFile = File(...),
    params: dict = Depends(params_styletransfer)
):
    """
    Post an image(.jpg ) to make it artistic-style. 
    You can get the artistic-style image using GET /image API. 
    """
    
    return await handler.post_file(
        "transferred-image",
        filerouter.processType.BYTESIO,
        file,
        **params
    )

