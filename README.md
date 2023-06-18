# StyleTransfer Server

Web-Server for Real Time Style Transfer.
The model used in this server is based on the paper 'A LEARNED REPRESENTATION FOR ARTISTIC STYLE' [https://arxiv.org/pdf/1610.07629.pdf], which enables the model to learn multiple styles and blend two styles for images.
To perform style transfer, users are required to select:

- Two styles you would like to blend
- A float value, alpha, that represents the weight of each style to be applied.

To use this server, you can utilize style-transfer models from repositories such as [https://github.com/ryanwongsa/Real-time-multi-style-transfer]. However, it is necessary to convert these models to onnx-style on this repository to utilize them in this server.

## API

| Route | Method | Query / Body | Description |
| --- | --- | --- | --- |
| /transferred-image | POST | - | Post an image to get styletransferred image. |

## How to use

### How to launch the Server

```bash
poetry install
poetry run python src/main.py --port 5555
```

### How to use the server from client

```bash
curl -X 'POST' \
  'http://localhost:3333/transferred-image?style1=1&style2=2&alpha=0.3&test=1' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@test_image.jpg;type=image/jpeg'
```

Here is python code example

```python

import requests

path_data = './temp'
fname_image = 'test_image.jpg'
params = {
  'style1': 1,
  'style2': 2,
  'alpha': 0.3
}
with open(f"{path_data}/{fname_image}", "rb") as _file:
    res = requests.post(
      'http://localhost:5555/transferred-image', \
      params = params, \
      files = {
        "file": (
            f"{fname_image}",
            file,
            "image/jpeg"
          )
      }
    )
```

## Examples  

The tranferred images can smoothly transition to the other styles.

!<img src="https://eye.kohei-kevin.com/wp-content/uploads/2023/03/247cf8ad-d8c5-41a7-bb99-14ed8031a719-1.png" alt="styletransfer1" title="styletransfer1">
