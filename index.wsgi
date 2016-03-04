
import sae
import web

from flaskDemo import app
from webpyDemo import app

    
application = sae.create_wsgi_app(app)