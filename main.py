from flask import Flask,render_template,request,jsonify
from controller import textToQr

# app init
app = Flask(__name__,static_url_path='', static_folder='public')

# main home path /
@app.route('/',methods=['GET'])
def home():
    return render_template("index.html")

# text to qr request 
@app.route('/get-qr',methods=['POST'])
def getQr():
    # get qr text from body 
    qrText = (request.get_json()["text"])

    try:
        # return this function 
        return textToQr(qrText)
    except Exception as e:
        # handle error
            return jsonify({"base64": None,"statusText": False,"message": "Server Error!"})


if __name__ == '__main__':
    app.run(host="0.0.0.0",port="3000",debug=True) # app running at http://localhost:3000