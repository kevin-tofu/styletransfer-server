import os
from typing import NamedTuple

VERSION = os.getenv('VERSION', 'v0'),
AUTHOR = os.getenv('AUTHOR', 'kevin')

APP_PORT = os.getenv('APP_PORT', 8000)

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


class Config(NamedTuple):
    app_port: int
    path_model: str
    path_data: str
    delete_intaval: int
    imsize_h: int
    imsize_w: int
    

config_org = Config(
    APP_PORT,
    PATH_MODEL,
    PATH_DATA,
    DELETE_INTERVAL,
    IMSIZE_H,
    IMSIZE_W
)
