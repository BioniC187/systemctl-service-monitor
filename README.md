# systemctl Service Monitor
Used to get the status of defined systemctl services and publish to a mqtt topic.

## get the repo
Download the repo into /home/systemctl-monitor
```
mkdir /home/systemctl-monitor
```
If you want to use a different directory, you will have to update the service file and the commands listed here to have the new path.

Go into the directory
```
cd /home/systemctl-monitor
```

download the code
```
wget https://github.com/BioniC187/systemctl-service-monitor/archive/refs/heads/feature/main.zip
```

extract the code
```
unzip -j main.zip
```

## Install dependencies
```
pip install -r requirements.txt
```

## config file
- interval - *time in seconds*
- mqttServer - *the ip address of the mqttbroker*
- mqttPort - *the port to use*
- mqttUsername - *mqtt broker username*
- mqttPassword - *mqttbroker password*
- deviceName - *this is used in the topicTemplate. no whitespace*
- topicTemplate - *the template of the topic that will be used*
- services - *comma seperated list of services that the script will monitor*

Refer to the file in the repo as an example.

## Install the service
```
cp /home/systemctl-monitor/systemctl-monitor.service /etc/systemd/system/systemctl-monitor.service
systemctl daemon-reload
systemctl start systemctl-monitor.service
systemctl status systemctl-monitor.service
```

