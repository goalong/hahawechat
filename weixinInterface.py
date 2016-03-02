# -*- coding: utf-8 -*-
import hashlib
import web
import time
import os
import urllib2,json
import pdb

urls = ('/wechat', 'WeixinInterface')

class WeixinInterface:
 
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)
 
    def GET(self):
        #获取输入参数
        data = web.input()
        if len(data) >= 2:
            # pdb.set_trace()
            signature=data.get(signature)
            timestamp=data.get(timestamp)
            nonce=data.get(nonce)
            echostr=data.get(echostr)
            #自己的token
            token="test"
            #字典序排序
            l=[token,timestamp,nonce]
            l.sort()
            s = l[0] + l[1] + l[2]
     
            #如果是来自微信的请求，则回复echostr
            if hashlib.sha1(s).hexdigest() == signature:
                return 'verify'
        return 'not verify'

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()