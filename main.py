import subprocess
from mqttService import MqttService
from serviceModel import Service
import configparser
import schedule
import time

config = configparser.ConfigParser()
config.read('config.ini')
defaultConfig = config['DEFAULT']

servicesToCheck = {}

if 'servicesFile' in defaultConfig:
  with open(defaultConfig['servicesFile']) as file:
     for line in file:
       line = line.rstrip()
       service = Service(line)
       servicesToCheck[service.serviceName] = service
       
else:
  servicesFromConfig = defaultConfig['services'].split(',')
  for svc in servicesFromConfig:
    service = Service(svc)
    servicesToCheck[service.serviceName] = service

def getServices():
  proc = subprocess.Popen("systemctl -t service --no-legend --no-pager --all", stdout=subprocess.PIPE, shell=True)
  output = proc.stdout.read()
  lines = output.splitlines()

  services = []
  servicesDict = {}
  payload = {}
  payload['data'] = []
  payload['deviceName'] = defaultConfig['deviceNameDisplayText']

  for line in lines:
    data = line.split()
    serviceName = data[0].decode('utf-8')
    service = servicesToCheck[serviceName]
    if service is not None:
      data = {
        'name': serviceName,
        'displayName': service.displayName,
        'loaded': data[1].decode('utf-8'),
        'active': data[2].decode('utf-8'),
        'sub': data[3].decode('utf-8')
      }
      services.append(data)
      payload['data'].append(data)
      servicesDict[serviceName] = data
  mqttService.publish(payload)  # data attribute
mqttService = MqttService(defaultConfig)
mqttService.start()

def worker():
  getServices()

schedule.every(int(defaultConfig['interval'])).seconds.do(worker)

while True:
  schedule.run_pending()
  time.sleep(1)
