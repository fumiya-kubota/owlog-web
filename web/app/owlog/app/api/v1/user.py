from sanic import Blueprint
from sanic import response
from owlog.app.model import User

user = Blueprint('users', url_prefix='/users')


@user.route('/', methods=['POST'])
async def test(request):
    data = request.json
    name = data.get('name')
    u1 = await User.create(name=name)
    return response.json(
        {'access_token': ''},
        status=200
    )


@user.route('/test')
async def test_api(request):
    return response.json(
        {'result': 'OK'},
        status=200
    )
