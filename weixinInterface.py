# encoding: utf-8

import hashlib
import web
import time
import os
import urllib2,json
import pdb
from lxml import etree

urls = ('/wechat', 'WeixinInterface')

class WeixinInterface:
 
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


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()