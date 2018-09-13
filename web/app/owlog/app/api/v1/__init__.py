from sanic import Blueprint
from .user import user

bp = Blueprint.group(user, url_prefix='/v1')
