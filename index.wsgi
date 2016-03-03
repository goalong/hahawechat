
import os
 
import sae
import web
 
from wechat import Wechat, AskAuth
 
urls = (
'/wechat','Wechat',
'/auth', 'AskAuth'
)
 
app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)
 
app = web.application(urls, globals()).wsgifunc()  
app.debug = True      
application = sae.create_wsgi_app(app)