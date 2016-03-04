
import sae
import web
from flaskDemo import app
from webpyDemo import Wechat, Auth, app

 
    
application = sae.create_wsgi_app(app)