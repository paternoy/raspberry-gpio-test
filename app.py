from flask import Flask,request,render_template, redirect, url_for
from OnOffButtonLed import OnOffButtonLed
import threading
import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
app = Flask(__name__)
onOff = OnOffButtonLed()

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/',methods=['POST'])
def post():
	print("Button Posted")
	onOff.toggle()
	return redirect('/')


if __name__ == '__main__':
#	t = threading.Thread(target=onOff.loop)
#	t.daemon=True
#	t.start()
	try:
		app.run(host='0.0.0.0',port=80,debug=False)
                #GPIO.cleanup() # cleanup all GPIO
	except KeyboardInterrupt:
		onOff.cleanup()
	finally:
		onOff.cleanup()
