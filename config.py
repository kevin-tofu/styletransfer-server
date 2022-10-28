import os


VERSION = os.getenv('VERSION', 'v0'),
AUTHOR = os.getenv('AUTHOR', 'kevin')

APP_PORT = os.getenv('APP_PORT', 80)

PATH_DATA = os.getenv('PATH_DATA', './temp')
PATH_MODEL = os.getenv('PATH_MODEL', './model')
MODEL_NAME = os.getenv('MODEL_NAME', './model.onnx')
DELETE_INTERVAL = os.getenv('DELETE_INTERVAL', 60)
