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

VD Guests

adafruit-pca9685
Adafruit-SSD1306
mpu6050-raspberrypi

sudo pip install adafruit-ads1x15

#audio config
cat /proc/asound/cards - to see the mic
pactl list
pacat -r --latency-msec=1 -d alsa_input.usb-C-Media_Electronics_Inc._USB_PnP_Sound_Device-00.analog-mono | pacat -p --latency-msec=1

#wireless config:
#sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

#permanent dev assingment or cameras
# https://unix.stackexchange.com/questions/77170/how-to-bind-v4l2-usb-cameras-to-the-same-device-names-even-after-reboot
# 1)
# sudo udevadm info --query=all --name=/dev/video2
# 2)
# sudo udevadm info -ap /devices/virtual/video4linux/video2


refresh dependency list
pipreqs --force ProgramaticallyAidedRCcar/wificar



#UARTS:
https://www.tomshardware.com/reviews/raspberry-pi-gpio-pinout,6122.html
https://www.raspberrypi.org/forums/viewtopic.php?t=244827


python --version
Python 2.7.15+
