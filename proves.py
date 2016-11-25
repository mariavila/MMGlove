from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)

socketio = SocketIO(app)

@app.route('/')
def hello_func():
    print ('ohayo')
	#return render_template('hello.html')

@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))

if __name__ == '__main__':
    socketio.run(app, '0.0.0.0', port=5000)
