from flask import Flask, request, Response, render_template
from flask.ext.socketio import SocketIO, emit
app = Flask(__name__)
socketio = SocketIO(app)

temperature = None
humidity = None

values = {
    'temp': 25,
    'hum': 0,
}

@app.route('/')
def index():
    return render_template('index.html', temp=values['temp'])

@app.route('/set/<float:temp>/<float:hum>',methods=['POST','GET'])
def set_values(temp,hum):
    global temperature, humidity
    temperature = float(request.args.get('temp'))
    humidity = float(request.args.get('hum'))
    values['temp'] = temperature
    values['hum'] = humidity
    return "hello_world"

@app.route('/get',methods=['GET'])
def get_values():
    global temperature, humidity
    return "temperature = " + str(temperature) + " | humidity = " + str(humidity)

@socketio.on('value changed')
def value_changed(message):
    values[message['who']] = message['data']
    emit('update value', message, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
