import flask as Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)


app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app)

import Visualization.app