from threading import Lock
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import sys
import model

async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()


@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)


@socketio.on('broadcast_event', namespace='')
def broadcast_message(message):
    note = message['data2']
    id = message['data']
    model.save(id, note)
    result = model.get_item(id)
    emit('response', {'data': result, 'id': id}, broadcast=True)


@socketio.on('delete_item', namespace="")
def delete_item(message):
    id = message["data"]
    model.delete_item(id)
    emit('delete_response', {'data': id}, broadcast=True)


@app.route("/view", methods=["POST"])
def get_item():
    id = request.form["id"]
    result = model.get_item(id)
    return render_template('view_one.html', v=result, flag=0)


@app.route("/view_all", methods=["POST"])
def get_items():
    result = model.get_items()
    return render_template('view_all.html', v=result)


@socketio.on('disconnect', namespace='')
def test_disconnect():
    print('Client disconnected', request.sid)


if __name__ == '__main__':
    socketio.run(app, debug=True)
