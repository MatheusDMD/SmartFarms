from flask import Flask, render_template, request
# from flask.ext.socketio import SocketIO, emit

app = Flask(__name__)
# socketio = SocketIO(app)

dic_farm = {'rachelpbm@gmail.com': 123456, 'matheus_dmd@gmail.com': 123456, 'gabi_almeida@gail.com' : 123456}
cord_lat = -23.61571
cord_lng = -47.1794659
sensor_location = "Plantação de soja"
sensor_humidity = "70%"

def __init__(self, email, password):
    self.email = email
    self.password = password

@app.route('/')
def index():
	return render_template('smartfarm_home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		print("tentativa login")
		# email = request.form["email"]
		# password = request.form["pwd"]
		# print(email)
		# print(password)
		
		# if dic_farm[email] == password:
		# 	print('sucesso no login')
		return render_template('smartfarm_user.html', lat= cord_lat, lng = cord_lng, location=sensor_location, humidity=sensor_humidity )

		# else:
		# 	print('login negado')
		# 	return render_template('smartfarm_home.html')
	else:
		return render_template('smartfarm_home.html')

# @socketio.on('value changed')
# def value_changed(message):
#     values[message['who']] = message['data']
#     emit('update value', message, broadcast=True)

if __name__ == '__main__':
	app.run(host='0.0.0.0')
#    socketio.run(app, host='0.0.0.0')
