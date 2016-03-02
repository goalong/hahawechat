
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

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()