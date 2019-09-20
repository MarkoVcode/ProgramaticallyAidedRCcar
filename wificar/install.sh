#!/bin/bash 
#https://www.dafont.com/
#https://www.linux-projects.org/uv4l/tutorials/play-retropie-in-browser/
#https://www.linux-projects.org/uv4l/tutorials/rpi-webapp-screen-audio-keyboard-sharing/
sudo apt-get install screen
pip install -r requirements.txt
#network-manager???
#sudo pip install adafruit-pca9685
#sudo pip install Adafruit-SSD1306
#sudo pip install mpu6050-raspberrypi
#sudo pip install adafruit-ads1x15 ADC

https://stackoverflow.com/questions/43319199/how-to-loop-back-the-microphone-entry-directly-to-speakers-on-linux/43319706
https://superuser.com/questions/87571/how-to-hear-mic-sound-over-speakers-ubuntu-karmic

adafruit-pca9685
Adafruit-SSD1306
mpu6050-raspberrypi

sudo pip install adafruit-ads1x15

{'y': -1.7812860351562498, 'x': -9.009380847167968, 'z': 2.2002713256835937}, '1w': '', 'gps': {'qqq': 'dds'}}
(producer ) Awaiting for the messages. 0 items in queue
(producer ) Returning sensors: {'accel': {'y': -1.7860744384765623, 'x': -9.016563452148437, 'z': 2.205059729003906}, '1w': '', 'gps': {'qqq': 'dds'}}
(producer ) Awaiting for the messages. 0 items in queue
(producer ) Returning sensors: {'accel': {'y': -1.7573440185546874, 'x': -9.368511096191405, 'z': 2.3151930053710936}, '1w': '', 'gps': {'qqq': 'dds'}}
(producer ) Awaiting for the messages. 0 items in queue
(producer ) Returning sensors: {'accel': {'y': -1.7094599853515624, 'x': -9.306261853027344, 'z': 2.4253262817382812}, '1w': '', 'gps': {'qqq': 'dds'}}
(producer ) Awaiting for the messages. 0 items in queue
(producer ) Returning sensors: {'accel': {'y': -1.7286135986328124, 'x': -9.311050256347656, 'z': 2.176329309082031}, '1w': '', 'gps': {'qqq': 'dds'}}
(producer ) Awaiting for the messages. 0 items in queue
(producer ) Returning sensors: {'accel': {'y': -1.6543933471679686, 'x': -9.074024291992187, 'z': 2.43250888671875}


pactl list
pacat -r --latency-msec=1 -d alsa_input.usb-C-Media_Electronics_Inc._USB_PnP_Sound_Device-00.analog-mono | pacat -p --latency-msec=1
