import os
# from typing import NamedTuple
from dataclasses import dataclass

VERSION = os.getenv('VERSION', 'v0'),
AUTHOR = os.getenv('AUTHOR', 'kevin')

APP_PORT = os.getenv('APP_PORT', 80)

PATH_DATA = os.getenv('PATH_DATA', './temp')
PATH_MODEL = os.getenv('PATH_MODEL', './model/model.onnx')
DELETE_INTERVAL = os.getenv('DELETE_INTERVAL', 60)
IMSIZE_H = os.getenv('IMSIZE_H', 512)
IMSIZE_W = os.getenv('IMSIZE_W', 512)

# config = dict(
#     PATH_DATA = PATH_DATA,
#     PATH_MODEL = PATH_MODEL,
#     DELETE_INTERVAL = DELETE_INTERVAL
# )

@dataclass
class Config():
    app_port: int
    version: str
    author: str
    path_model: str
    path_data: str
    delete_intaval: int
    imsize_h: int
    imsize_w: int
    

config_org = Config(
    APP_PORT,
    VERSION,
    AUTHOR,
    PATH_MODEL,
    PATH_DATA,
    DELETE_INTERVAL,
    IMSIZE_H,
    IMSIZE_W
)
