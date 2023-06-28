# poolmonitor, a collection of data logging utilities

Currently just logging a temperature probe on both my hot tub and my pool.

How does it work?

Raspberry Pi 3 + Temerature Probe => Python3 Script => Send Data to IoTPlotter.com to log it


## Install

### Step 1 - Clone the repository
```
cd ~; git clone https://github.com/grumpymaker/poolmonitor.git
```

### Step 2 - IoTPlotter.com

* Create an account
* Create an API Key
* Create a feed and name a sensor.

### Step 3 - Edit Settings

Add the following to your profile (e.g. ~/.profile, ~/.bashrc, etc):
```
export SENSORPATH="/sys/bus/w1/devices/28-SOME_DEVICE_ID_HERE/w1_slave"
export IOTPLOTTERAPI="API_KEY_HERE"
export IOTPLOTTERFEED="http://iotplotter.com/api/v2/feed/FEED_ID_HERE"
export MAKEWEBHOOK="MAKE_WEBHOOK_HERE"
```

Source the profile and/or logout and log back into SSH.

### Step 3 - Test run the script

See if the data shows up in the IoTPlotter Feed.
```
python3 ~/poolmonitor/iotplotter.py
```

### Step 4 - Set a cronjob to run it periodically

```
crontab -e

*/5 * * * * python3 /home/pi/poolmonitor/iotsender.py
```
