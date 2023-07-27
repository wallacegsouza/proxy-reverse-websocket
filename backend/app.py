from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import json


app = Flask(__name__)
CORS(app)
resources = {r"/api/*": {"origins": "*"}}
app.config["CORS_HEADERS"] = "Content-Type"
app.config['JSON_SORT_KEYS'] = False
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app, async_mode=None)

@app.route('/api')
def home():
    return jsonify({"Message":"This is your flask app with docker"})

@socketio.event
def my_event(message):
    print("my_event" + str(message))
    emit('my response', {'data': 'got it!'})

@socketio.on('message', namespace="/test")
def handle_message(data):
    print('received message: ' + data)

if __name__ == "__main__":
    # app.run(debug = True, host='0.0.0.0', port=7007)
    socketio.run(app, host="0.0.0.0", port=5000, allow_unsafe_werkzeug=True)
    # socketio.run(app, path="/socket/", host="0.0.0.0", port=5000, allow_unsafe_werkzeug=True)