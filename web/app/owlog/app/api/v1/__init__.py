from sanic import Blueprint
from .user import user
from .signin import signin


bp = Blueprint.group(user, signin, url_prefix='/v1')
