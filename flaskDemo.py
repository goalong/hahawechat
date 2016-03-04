# encoding: utf-8

import time
from flask import Flask, request, make_response
import hashlib
import xml.etree.ElementTree as ET
from settings import APPID, APPSECRET, SCOPE, REDIRECT_URI, URL
import urllib2
import json
import pdb

app = Flask(__name__)
app.debug=True
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

    code = request.args.get('code', '')
    return code
    # url = 'https://api.weixin.qq.com/sns/oauth2/access_token?appid={APPID}&secret={SECRET}&code={CODE}&grant_type=authorization_code'.format(
    #         APPID=APPID, SECRET=APPSECRET, CODE=code)
    # content = urllib2.urlopen(url).read()
    # content = json.loads(content)
    # return content, code, data

    # access_token = content['access_token']
    # openid = content['openid']
    # url2 = 'https://api.weixin.qq.com/sns/userinfo?access_token={ACCESS_TOKEN}&openid={OPENID}&lang=zh_CN'.format(ACCESS_TOKEN=access_token, OPENID=openid)
    # userinfo = json.loads(urllib2.urlopen(url2).read())
    # return render.auth(userinfo['nickname'], userinfo['city'], userinfo['country'], userinfo['province'])





if __name__ == '__main__':
    app.run()