import os

from flask import Flask, send_file
import flask
import base64
from StegHelper import Steganography

app = Flask(__name__)


@app.route('/')
def hello_world():
    print("gg")
    return 'Hello World!'

@app.route('/upload',methods=["POST"])
def upload():
    print('ggg')
    im=flask.request.values.get('image')
    password=flask.request.values.get('password')
    type=flask.request.values.get('type')
    outputpath="/home/shubhamjuneja11/"+password+'.'+type
    inputpath="/home/shubhamjuneja11/input"+'.'+type
    with open(inputpath, "wb") as fh:
        fh.write(base64.decodestring(im))
    name=flask.request.values.get('name')
    Steganography.encode(inputpath,outputpath,name)
    print('done')


    with open(outputpath, "rb") as f:
        data = f.read()
    #print(decoded)
    print(data.encode('base64')) 
    return data.encode('base64')

@app.route('/decode',methods=["POST"])
def decodeimage():
    print("fff")
    im = flask.request.values.get('image')
    password = flask.request.values.get('password')
    type = flask.request.values.get('type')
    outputpath = "/home/shubhamjuneja11/" + password + '.' + type
    print(outputpath)
    if(os.path.exists(outputpath)):

            with open(outputpath, "wb") as fh:
                fh.write(base64.decodestring(im))
            secret=Steganography.decode(outputpath)
            return secret
    else:
            return "sorry"

if __name__ == '__main__':
    app.run(host='192.168.43.75',port='5000')
