
import sae
import web

from webpyDemo import Wechat, Auth, app
from flaskDemo import app
 
    
application = sae.create_wsgi_app(app)