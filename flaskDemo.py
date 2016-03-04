# encoding: utf-8

import time
from flask import Flask, request, make_response
import hashlib
import xml.etree.ElementTree as ET
from settings import APPID, APPSECRET, SCOPE, REDIRECT_URI, URL
import urllib2
import json
from webpyDemo import get_userinfo
import pdb

app = Flask(__name__)
app.debug=True
@app.route('/')
def index():
    return 'Weclome'

# 服务器验证
@app.route('/wechat', methods=['GET', 'POST'])
def wechat_verify():
    if request.method == 'GET':
        token = 'test'  
        query = request.args
        signature = query.get('signature', '')
        timestamp = query.get('timestamp', '')
        nonce = query.get('nonce', '')
        echostr = query.get('echostr', '')
        s = [timestamp, nonce, token]
        s.sort()
        s = ''.join(s)
        if (hashlib.sha1(s).hexdigest() == signature):
            return echostr
        return u'验证失败'
    else:
        xml_recv = ET.fromstring(request.data)    #XML数据存储在request.data中
        ToUserName = xml_recv.find("ToUserName").text
        FromUserName = xml_recv.find("FromUserName").text
        Content = xml_recv.find("Content").text
        reply = '''<xml><ToUserName><![CDATA[%s]]></ToUserName>
                    <FromUserName><![CDATA[%s]]></FromUserName>
                    <CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType>
                    <Content><![CDATA[%s]]></Content><FuncFlag>0</FuncFlag></xml>'''
        response = make_response(reply % (FromUserName, ToUserName,
                                          str(int(time.time())), Content))
        response.content_type = 'application/xml'
        return response
# 网页授权
@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if request.method == 'GET':
        code = request.args.get('code', '')
        userinfo = get_userinfo(code)
        return userinfo.get('nickname', '')+'\nhaha' + userinfo.get('city', '')







# if __name__ == '__main__':
#     app.run()