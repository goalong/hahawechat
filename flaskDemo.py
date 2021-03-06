# encoding: utf-8

import time
from flask import Flask, request, make_response, render_template
import hashlib
import xml.etree.ElementTree as ET
from settings import APPID, APPSECRET, SCOPE, REDIRECT_URI, URL
import urllib2
import json
from webpyDemo import get_userinfo
import random


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
        reply_list = [u'呵呵', u'干嘛', u'Sorry, 去洗澡了。。。', u'你说什么，大声点', u'哦']
        response = make_response(reply % (FromUserName, ToUserName,
                                          str(int(time.time())), random.choice(reply_list)))
        response.content_type = 'application/xml'
        return response
# 网页授权
@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if request.method == 'GET':
        code = request.args.get('code', '')
        userinfo = get_userinfo(code)
        return render_template("welcome.html",
                    unionid=userinfo.get('unionid', u'无'),
                    sex = userinfo.get('sex', u'未知'),
                    userinfo = userinfo)


# if __name__ == '__main__':
#     app.run()