from sanic import Blueprint
from sanic.response import json


signin = Blueprint('signin', url_prefix='/signin')


@signin.route('/')
async def test(request):
    return json({'hello': 'api'})
