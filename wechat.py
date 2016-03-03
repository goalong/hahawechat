# encoding: utf-8

import hashlib
import web
import time
import os
import urllib2,json
from lxml import etree
from urllib import urlencode
import json
import pdb

urls = (
    '/wechat', 'Wechat',
    '/auth', 'AskAuth'
    )
APPID = 'wx25fa28a3f4439fe2'
APPSECRET = '1443a06f8c87f0f7889cc898d516f588'
SCOPE = 'snsapi_userinfo'
REDIRECT_URI = 'http://hahawechat.applinzi.com/auth'
URL = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid={APPID}&redirect_uri={REDIRECT_URI}&response_type=code&scope={SCOPE}&state=STATE#wechat_redirect'.format(
            APPID=APPID, REDIRECT_URI=REDIRECT_URI, SCOPE=SCOPE)


render = web.template.render('templates')

class Wechat:
 
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)
 
    def GET(self):
        data = web.input()
        signature=data.get('signature')
        timestamp=data.get('timestamp')
        nonce=data.get('nonce')
        echostr=data.get('echostr')

        token="test"

        if len(data) >= 2 and signature and timestamp and nonce:
            
            l=[token,timestamp,nonce]
            l.sort()
            s = l[0] + l[1] + l[2]
            if hashlib.sha1(s).hexdigest() == signature:
                return echostr
        # pdb.set_trace()
        return data

    def POST(self):        
        str_xml = web.data() #获得post来的数据
        xml = etree.fromstring(str_xml)#进行XML解析
        content=xml.find("Content").text#获得用户所输入的内容
        msgType=xml.find("MsgType").text
        fromUser=xml.find("FromUserName").text
        toUser=xml.find("ToUserName").text
        return self.render.reply_text(fromUser,toUser,int(time.time()),u'我知道你说的是{content}, 但我还不确定回复你什么呢。Not Sure Yet.'.format(content=content))

class WechatAuth():
    def GET(self):
        pass
    def POST(self):
        pass
class AskAuth():
    def GET(self):
        data = web.input()
        # print data
        # pdb.set_trace()
        code = data.code
        url = 'https://api.weixin.qq.com/sns/oauth2/access_token?appid={APPID}&secret={SECRET}&code={CODE}&grant_type=authorization_code'.format(
                APPID=APPID, SECRET=APPSECRET, CODE=code)
        content = urllib2.urlopen(url).read()
        content = json.loads(content)
        access_token = content['access_token']
        openid = content['openid']
        url2 = 'https://api.weixin.qq.com/sns/userinfo?access_token={ACCESS_TOKEN}&openid={OPENID}&lang=zh_CN'.format(ACCESS_TOKEN=access_token, OPENID=openid)
        userinfo = json.loads(urllib2.urlopen(url2).read())
        return render.auth(userinfo['nickname'], userinfo['city'], userinfo['country'], userinfo['province'])
    def POST(self):
        pass


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()