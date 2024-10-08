from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('chat.html')

@socketio.on('message')
def handle_message(data):
    user = data['user']
    message = data['text']
    print('Message received from {}: {}'.format(user, message))
    emit('message', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
