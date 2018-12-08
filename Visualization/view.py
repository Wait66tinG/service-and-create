#!/usr/bin/env python
from flask import render_template
from flask_socketio import emit
from Visualization import app, socketio


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test1')
def screen():
    return app.send_static_file('test1.html')

@socketio.on('client_event')
def client_msg(msg):
    emit('server_response', {'data': msg['data']})
    
@socketio.on('connect_event')
def connected_msg(msg):
    emit('server_response', {'data': msg['data']})

