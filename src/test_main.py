# import sys
# sys.path.append('../..')
from fastapi.testclient import TestClient
from config import config_org as config

path_data = config.path_data
name_video = 'test_video.mp4'
name_image = 'test_image.jpg'
name_image_wrong = 'test_image.jp'


from main import app
testclient = TestClient(app)


def test_read_main():
    res = testclient.get('')
    assert res.status_code == 200
    assert type(res.json()) == dict


def test_image():

    path_image = f"{path_data}/{name_image}"
    print('path_image:', path_image)
    with open(path_image, "rb") as _file:
        res = testclient.post("/transferred-image?test=1", files={"file": (f"_{name_image}", _file, "image/jpeg")})
    
    print(res)
    assert res.status_code == 200
    # assert type(res.json()) == dict

if __name__ == "__main__":

    test_read_main()

    test_image()
    
#     test_video()
    