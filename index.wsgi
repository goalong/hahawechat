
import os
 
import sae
import web
 
from wechat import Wechat, Auth
 
urls = (
'/wechat','Wechat',
'/auth', 'Auth'
)
 
render = web.template.render('templates')
 
app = web.application(urls, globals()).wsgifunc()  
app.debug = True      
application = sae.create_wsgi_app(app)