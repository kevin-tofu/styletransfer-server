
import os
from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.cors import CORSMiddleware

from routes import styletransfer
import config


# app = FastAPI()
app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

origins = ["*"]
# origins = [
#     "http://localhost",
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


serverinfo = {
    "version": config.VERSION,
    "author": config.AUTHOR
}

@app.get("/")
def root():
    return serverinfo

app.include_router(styletransfer.router)

if __name__ == "__main__":

    
    import uvicorn
    import argparse

    myport = config.APP_PORT
    print("myport", myport)

    parser = argparse.ArgumentParser()
    parser.add_argument('--gpu', '-G', type=int, default='-1', help='gpu number')
    parser.add_argument('--port', '-P', type=int, default=myport, help='port for http server')
    args = parser.parse_args()

    uvicorn.run('main:app', host="0.0.0.0", port=args.port)