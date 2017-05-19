from flask import Flask, render_template
from flask_socketio import SocketIO
import threading

def runFunc():
    socketio.run(app)

app = Flask(__name__)
socketio = SocketIO(app)
thread = threading.Thread(None, runFunc)

@app.route('/')
def hello_func():
    #print ('ohayo')
    return render_template('hello.html')

@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))
    socketio.emit('ping event', {'data': 42})

if __name__ == '__main__':
    thread.start()
    while 1:
        inp = raw_input()
        if inp == 'a':
            socketio.emit('ping event', {'data': 42})
