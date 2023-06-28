 # poolmonitor, a collection of data logging utilities

Currently just logging a temperature probe on both my hot tub and my pool.

How does it work?

Raspberry Pi 3 + Temperature Probe => Python3 Script => Send Data to IoTPlotter.com to log it

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
export IOTPLOTTERSENSOR="POOL_TEMP"
export MAKEWEBHOOK="MAKE_WEBHOOK_HERE"
```

Source the profile and/or logout and log back into SSH.

### Step 4 - Test run the script

See if the data shows up in the IoTPlotter Feed.
```
python3 ~/poolmonitor/iotplotter.py
```

### Step 5 - Set a cronjob to run it periodically

```
crontab -e

*/5 * * * * . /home/pi/.profile; python3 /home/pi/poolmonitor/iotsender.py
```

## Hardware

Sourced from anywhere:
* Raspberry Pi 3 B+, 4, etc (install raspbian, enable ssh, update and secure, install python3 / python3-pip, pip install requests, etc)
* Case for the RPi (nice to have)
* Power supply for RPi

Adafruit Parts:
* 1 x Large Plastic Project Enclosure - Weatherproof with Clear Top[ID:905] = $19.95
  * https://www.adafruit.com/product/905
* 1 x Waterproof DS18B20 Digital temperature sensor + extras[ID:642] = $14.95
  * https://www.adafruit.com/product/642
* 1 x Half-size breadboard[ID:64] = $5.00
  * https://www.adafruit.com/product/64
* 1 x Adafruit Pi T-Cobbler Plus Kit Breakout for 2x20 Raspberry Pi [ID:1989] = $7.50
  * https://www.adafruit.com/product/1989

Hardware setup guide: https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/hardware
> If you are using the "high temperature" version of the DS18B20 we sell, connect Orange Stripe to 3.3V, White connects to ground and Blue Stripe is data, pin #4.

> You still need a ~4.7K-10K resistor from data to 3.3V
  
