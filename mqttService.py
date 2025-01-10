import paho.mqtt.client as mqtt
import json

class MqttService:
  def __init__(self, config):
    self.config = config
    self.init()

  def init(self):
    self.publishTopic = self.config['topicTemplate'].replace('{{deviceNameForTopic}}', self.config['deviceNameForTopic'])
    self.client = mqtt.Client(client_id="", userdata=None, protocol=mqtt.MQTTv5)
    self.client.username_pw_set(self.config['mqttUsername'], self.config['mqttPassword'])
    self.client.connect(self.config['mqttServer'], int(self.config['mqttPort']), 60)

  def publish(self, data):
    self.client.publish(self.publishTopic, json.dumps(data), qos=0)

  def start(self, background=True):
    if(background):
      self.client.loop_start()
    else:
      self.client.loop_forever()
