from flask import Flask, render_template, url_for, redirect
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['DEBUG'] = True
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/orginate')
def orginate():
    socketio.emit('server orginated', 'Something happened on the server')
    return '<h1>Sent!</h1>'

@app.route('/home', methods=["GET", "POST"])
def home():
    return render_template('home.html')

@socketio.on('message from user')
def receive_message_from_user(message):
    print ('USER MESSAGE {}'.format(message))
    #emit ('from Flask', message.upper(), broadcast=True) ****** WHY THIS WAY DOESN'T WORK? BTW NO ERROR MESSAGE IS RAISED *******
    emit('redirect', {'url': url_for('home')}, broadcast=True)


if __name__ == '__main__':
    socketio.run(app)
