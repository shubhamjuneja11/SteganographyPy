import os

from flask import Flask, send_file
import flask
import base64
import Helper
from flask import jsonify

app = Flask(__name__)
import random
mp={}
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
passlen = 15

@app.route('/')
def hello_world():
    print("gg")
    return 'Hello World!'

@app.route('/upload',methods=["POST"])
def upload():
    global mp
    print('ggg')
    im=flask.request.values.get('image')
    password=flask.request.values.get('password')
    p = "".join(random.sample(s, passlen))
    mp[p]=password
    outputpath="/home/shubhamjuneja11/friends.png"
    inputpath="/home/shubhamjuneja11/outputzzz.png"
    with open(inputpath, "wb") as fh:
        fh.write(base64.decodestring(im))

    print('image')
    name=flask.request.values.get('name')

    Helper.encode(inputpath,outputpath,name)
    print('done')


    with open(outputpath, "rb") as f:
        data = f.read()
    #print(decoded)
    res={}
    res['image']=data.encode('base64')
    res['name']=p+'.png'
    return jsonify(res)

@app.route('/decode',methods=["POST"])
def decodeimage():
    print("fff")
    global mp
    im = flask.request.values.get('image')
    password = flask.request.values.get('password')

    name=flask.request.values.get('name')
    outputpath = "/home/shubhamjuneja11/friends.png"
    with open(outputpath, "rb") as f:
        data = f.read()
    print('gg')
    print(name)
    pw=mp[name]
    secret='Wrong Password'
    if(pw==password):
        with open(outputpath, "wb") as fh:
            fh.write(base64.decodestring(im))
        secret=Helper.decode(outputpath)
    return secret

if __name__ == '__main__':
    app.run(host='192.168.0.105',port='5000')
