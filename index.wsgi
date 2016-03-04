
import sae
import web
 
from wechat import Wechat, Auth, app
 
app = app.wsgifunc()       
application = sae.create_wsgi_app(app)