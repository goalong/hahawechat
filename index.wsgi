
import sae
import web
from webpyDemo import Wechat, Auth, app
app = app.wsgifunc()   
from flaskDemo import app
 
    
application = sae.create_wsgi_app(app)