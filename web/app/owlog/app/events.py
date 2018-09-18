from sanic import Blueprint
from .model import db

events = Blueprint('events')


@events.listener('before_server_start')
async def setup_connection(app, loop):
    await db.set_bind(f"{app.config['DATABASE_SERVER']}/{app.config['DATABASE_NAME']}")
