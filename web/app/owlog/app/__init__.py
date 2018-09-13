from sanic import Sanic
from .api import api
from .config import get_configuration_object

app = Sanic(__name__)
app.config.from_object(get_configuration_object())
app.blueprint(api)
