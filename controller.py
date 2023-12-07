import uuid
import base64
import os
import qrcode
from flask import jsonify


# qr initsalisation
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2,
)

# image to base64 converter
def image_to_base64_url(file_path):
    with open(file_path, "rb") as image_file:
        # Read the image file
        image_content = image_file.read()

        # Encode the image content in Base64
        encoded_image = base64.b64encode(image_content).decode("utf-8")

        # Determine the image format based on the file extension
        image_format = file_path.split('.')[-1]

        # Create the data URL
        data_url = f"data:image/{image_format};base64,{encoded_image}"

        return data_url

def createQr(text):
    # create a uniq id  for filename
    filename = "/"+str(uuid.uuid4())+".png"
    # full path
    path = "./public"+filename;
    # create qr 
    qr.add_data(text)
    qr.make(fit=True)
    # qr config 
    img = qr.make_image(fill_color="black", back_color="white")
    # save image 
    img.save(path)
    # return full path
    return path


# request starting from here 
def textToQr(qrText):
    # text length validation
    if len(qrText)>500:
        return jsonify({"base64": None,"statusText": False,"message": "text length executed."})

    # creating qr and getting path
    path = createQr(qrText)

    # image path to base64 convert 
    urlData = image_to_base64_url(path)

    # after converting delete file
    os.unlink(path)

    # return success response 
    return jsonify({"base64": urlData,"statusText": True,"message": "QR has been generated."})
