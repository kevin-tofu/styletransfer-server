# StyleTransfer Server
 Web-Server for Real Time Style Transfer.
The model in this server is based on the paper 'A LEARNED REPRESENTATION FOR ARTISTIC STYLE' [https://arxiv.org/pdf/1610.07629.pdf]. 
This model learns multiple styles and mixes 2 styles for images.  
The users choose 
  * 2 styles which users would like to mix
  * float value, alpha that represents how much weight for each styles you would like to put on

You can learn style-transfer model using some repositories like below.   
[https://github.com/ryanwongsa/Real-time-multi-style-transfer]

But essentially, you have to convert the models to onnx-style on this repository.  

## API

| Route | Method | Query / Body | Description |
| --- | --- | --- | --- |
| /transfer-image | POST | - | Post an image to get styletransferred image. |
