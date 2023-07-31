from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO
from apscheduler.schedulers.background import BackgroundScheduler
import random
import json

app = Flask(__name__)
# CORS(app, resources={r"/*":{"origins":"*"}})
app.config["CORS_HEADERS"] = "Content-Type"
app.config['JSON_SORT_KEYS'] = False
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app, cors_allowed_origins="*", logger=True, engineio_logger=True)

@socketio.on('connect')
def connect():
    print("Client connection")

@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)

def count():
    """Funtion for teste """
    print('Scheduler is alive!')
    num = int(random.random() * 10000)
    print('echo num ' + str(num))
    socketio.emit('echo', {"data": num})

sched = BackgroundScheduler({'daemon': True, 'apscheduler.timezone': 'Europe/London'})
sched.add_job(count, 'interval', seconds=5)
sched.start()

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=8000, debug=True)