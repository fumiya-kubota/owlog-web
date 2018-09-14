from sanic import Blueprint
from app.model import db

events = Blueprint('events')


@events.listener('before_server_start')
async def setup_connection(app, loop):
    await db.set_bind(app.config['DATABASE_URI'])
