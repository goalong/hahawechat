# encoding: utf-8
import requests
import codecs
f = codecs.open(u'post.xml', u'r', u'utf-8')
content = u''.join(f.readlines())
f.close()
res = requests.post(u'http://hahawechat.applinzi.com/wechat', data=content.encode(u'utf-8'))
print res.text