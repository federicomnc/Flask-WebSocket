from flask import Flask, render_template, url_for, redirect
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['DEBUG'] = True
socketio = SocketIO(app)

@app.route('/', methods=["GET", "POST"])
def home():
    return render_template('index.html')

@app.route('/chivuolgiocare', methods=["GET", "POST"])
def chivuolgiocare():
    return render_template('chivuolgiocare.html')

@socketio.on('inizia il gioco')
def receive_message_from_user():
    print('INIZIA IL GIOCO')
    emit('redirect', {'url': 'chivuolgiocare'}, broadcast=True)

@socketio.on('nome')
def input_nome():
    print('***NOME***')

if __name__ == '__main__':
    socketio.run(app)