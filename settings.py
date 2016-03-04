# encoding: utf-8
'''
项目的设置，包括appid, appsecret, scope, redirect_uri等
'''

APPID = 'wx25fa28a3f4439fe2'
APPSECRET = '1443a06f8c87f0f7889cc898d516f588'
SCOPE = 'snsapi_userinfo'
REDIRECT_URI = 'http://hahawechat.applinzi.com/auth'
URL = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid={APPID} \
            &redirect_uri={REDIRECT_URI}&response_type=code&scope={SCOPE}&state=STATE#wechat_redirect'.format(
            APPID=APPID, REDIRECT_URI=REDIRECT_URI, SCOPE=SCOPE)
