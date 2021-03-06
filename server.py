from flask import Flask, render_template, request, jsonify, Response
import time
#from flask_socketio import SocketIO, emit

app = Flask(__name__)
#socketio = SocketIO(app)

dic_farm = {'rachelpbm@gmail.com': 123456, 'matheus_dmd@gmail.com': 123456, 'gabi_almeida@gail.com' : 123456}
cord_lat = -23.61571
cord_lng = -47.1794659
sensor_location = "Bonsai do Dias"
sensor_humidity = 70
irrigation_status = "0"
humidity_values = []

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
		return render_template('smartfarm_user.html', lat= cord_lat, lng = cord_lng, location=sensor_location )

		# else:
		# 	print('login negado')
		# 	return render_template('smartfarm_home.html')
	else:
		return render_template('smartfarm_home.html')
#
# @socketio.on('changed')
# def value_changed(message):
#     message['who'] = message['data']
#     print("chnaged")
#     socketio.emit('update', message, broadcast=True)
#
@app.route('/set',methods=['GET'])
def set_values():
	global sensor_humidity, irrigation_status, humidity_values
	sensor_humidity = request.args.get('hum')
	if int(sensor_humidity) > 900:
		humidity_values.append(sensor_humidity)
		if len(humidity_values)>5:
			irrigation_status = "1"
			return "1"
	else:
		humidity_values = []
	irrigation_status = "0"
	return "0"
 
@app.route("/stream")
def subscribe():
	def gen():
		while True:
			global sensor_humidity,irrigation_status
			time.sleep(1)
			print(irrigation_status)
			result = "data: {0},{1}\n\n".format(sensor_humidity, irrigation_status)
			yield result
	return Response(gen(), mimetype="text/event-stream")
#
# @app.route("/stream",methods=['GET'])
# def subscribe():
# 	def eventStream():
# 		while True:
# 			global sensor_humidity
# 			yield "humidity : {0}".format(sensor_humidity)

	return Response(eventStream(), mimetype="text/event-stream")
	#return jsonify(hum=sensor_humidity)

if __name__ == '__main__':
	app.run(host='0.0.0.0', threaded=True)
	#socketio.run(app , host='0.0.0.0')
