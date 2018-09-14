from sanic import Blueprint
from sanic import response

user = Blueprint('users', url_prefix='/users')


@user.route('/', methods=['POST', 'GET'])
async def test(request):
    return response.json(
        {'access_token': ''},
        status=200
    )
