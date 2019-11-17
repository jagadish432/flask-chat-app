from flask import Flask, render_template
from flask_socketio import SocketIO
from config import *

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
# app.config['FLASK_ENV'] = FLASK_ENV
app.config['ENV'] = FLASK_ENV
socketio = SocketIO(app)


@app.route('/')
def sessions():
    return render_template('session.html')


def message_received(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=message_received)


if __name__ == '__main__':
    socketio.run(app, debug=True, port=5010)
