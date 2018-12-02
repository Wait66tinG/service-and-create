"""
This script runs the FlaskWebProject1 application using a development server.
"""

from os import environ
from Visualization import app, socketio

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST','0.0.0.0')
    try:
        PORT = int(environ.get('SERVER_PORT', '5001'))
    except ValueError:
        PORT = 80
    socketio.run(app, host=HOST, port=PORT, threaded=True)
    #app.run()