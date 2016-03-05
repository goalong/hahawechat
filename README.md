###Usage
扫码关注，然后扫码同意网页授权，即可获取扫码者基本信息

![Follow me](https://github.com/goalong/hahawechat/tree/master/img/followMe.jpeg)
![AUTH](https://github.com/goalong/hahawechat/tree/master/img/auth.png)

###About
该项目实现了简易的自动回复和网页授权后展示用户信息。包含两个Demo，一个用的flask，一个用的webpy,网上有相关的webpy版本的实现，做为参考并加以改变，服务器用的sae,网页授权是用的测试帐号开发的。

默认使用的是Flask版本的，如果想切换为webpy的，只要在index.wsgi这个文件中改变一下from webpyDemo import app 和 from flaskDemo import app的次序即可。详情请参考[微信开发者文档](http://mp.weixin.qq.com/wiki/home/).
