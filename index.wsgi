
import sae
import web

from flaskDemo import app

    
application = sae.create_wsgi_app(app)