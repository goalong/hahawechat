import sae
from hello import app

application = sae.create_wsgi_app(app)