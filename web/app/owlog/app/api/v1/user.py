from sanic import Blueprint
from sanic.response import json


user = Blueprint('users', url_prefix='/users')


@user.route('/')
async def test(request):
    return json({'hello': 'api'})
