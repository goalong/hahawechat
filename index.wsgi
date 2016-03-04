
import sae
import web

from webpyDemo import Wechat, Auth, app
app.debug = True
app = app.wsgifunc()   

 
    
application = sae.create_wsgi_app(app)