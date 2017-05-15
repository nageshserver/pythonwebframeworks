import time
import paho.mqtt.client as mqttt
from flask import Flask, render_template ,request
app = Flask(__name__)

@app.route('/')
def home_page():
   return render_template('hello.html')

@app.route('/blink_led',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form['led']
      mqttc=mqttt.Client()
      mqttc.connect("broker.hivemq.com",1883,60)
      mqttc.loop_start()
      mqttc.publish("ESP8266/LED1",result)
      mqttc.loop_stop()
      mqttc.disconnect()
      if result == str(0):
         return "<html><body><h1>LED is off</h1></body></html>"
      else:
         return "<html><body><h1>LED is on</h1></body></html>"
   else:
      return "Check method of url"

        



if __name__ == '__main__':
   app.run(debug = True)
