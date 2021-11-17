import os


VERSION = os.getenv('VERSION', 'v0'),
AUTHOR = os.getenv('AUTHOR', 'kevin')

APP_PORT = os.getenv('APP_PORT', 80)

PATH_DATA = os.getenv('PATH_DATA', './temp/')
MONGODB_URL = os.getenv('MONGODB_URL', 'mongodb://localhost:27017/')
MONGODB_DATABASE = os.getenv('MONGODB_DATABASE', 'styletransfer')
MONGODB_COLLECTION = os.getenv('MONGODB_COLLECTION', 'images')

DELETE_INTERVAL = os.getenv('DELETE_INTERVAL', 60)
