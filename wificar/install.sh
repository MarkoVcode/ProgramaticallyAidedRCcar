#!/bin/bash

pip install python-wifi

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

sudo nmap -sn 10.0.2.0/24

#wireless config:
#sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

#permanent dev assingment or cameras
# https://unix.stackexchange.com/questions/77170/how-to-bind-v4l2-usb-cameras-to-the-same-device-names-even-after-reboot
# 1)
# sudo udevadm info --query=all --name=/dev/video2
# 2)
# sudo udevadm info -ap /devices/virtual/video4linux/video2
# lrwxrwxrwx 1 root root 6 Nov  8 16:17 /dev/camerafback -> video1 - console stream video

# video5
 


refresh dependency list generation
pipreqs --force ProgramaticallyAidedRCcar/wificar



#UARTS:
https://www.tomshardware.com/reviews/raspberry-pi-gpio-pinout,6122.html
https://www.raspberrypi.org/forums/viewtopic.php?t=244827


python --version
Python 2.7.15+




dmesg --follow


[ 8689.100096] usb 1-1.4: new high-speed USB device number 3 using xhci_hcd
[ 8689.263726] usb 1-1.4: New USB device found, idVendor=05a3, idProduct=9422, bcdDevice= 1.00
[ 8689.263742] usb 1-1.4: New USB device strings: Mfr=2, Product=1, SerialNumber=3
[ 8689.263755] usb 1-1.4: Product: H264 USB Camera
[ 8689.263767] usb 1-1.4: Manufacturer: Sonix Technology Co., Ltd.
[ 8689.263779] usb 1-1.4: SerialNumber: SN0001
[ 8689.359353] uvcvideo: Found UVC 1.00 device H264 USB Camera (05a3:9422)
[ 8689.397038] uvcvideo: Unable to create debugfs 1-3 directory.
[ 8689.397203] uvcvideo 1-1.4:1.0: Entity type for entity Extension 4 was not initialized!
[ 8689.397210] uvcvideo 1-1.4:1.0: Entity type for entity Extension 3 was not initialized!
[ 8689.397216] uvcvideo 1-1.4:1.0: Entity type for entity Processing 2 was not initialized!
[ 8689.397222] uvcvideo 1-1.4:1.0: Entity type for entity Camera 1 was not initialized!
[ 8689.397374] input: H264 USB Camera: USB Camera as /devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.4/1-1.4:1.0/input/input2
[ 8689.397547] usbcore: registered new interface driver uvcvideo
[ 8689.397551] USB Video Class driver (1.1.1)
[ 8689.426815] usb 1-1.4: 4:1: cannot get freq at ep 0x84
[ 8689.547900] usbcore: registered new interface driver snd-usb-audio








[ 8768.574686] usb 1-1.3: new high-speed USB device number 4 using xhci_hcd
[ 8768.738371] usb 1-1.3: New USB device found, idVendor=05a3, idProduct=9422, bcdDevice= 1.00
[ 8768.738388] usb 1-1.3: New USB device strings: Mfr=2, Product=1, SerialNumber=3
[ 8768.738401] usb 1-1.3: Product: H264 USB Camera
[ 8768.738413] usb 1-1.3: Manufacturer: Sonix Technology Co., Ltd.
[ 8768.738424] usb 1-1.3: SerialNumber: SN0001
[ 8768.756575] uvcvideo: Found UVC 1.00 device H264 USB Camera (05a3:9422)
[ 8768.795003] uvcvideo: Unable to create debugfs 1-4 directory.
[ 8768.795811] uvcvideo 1-1.3:1.0: Entity type for entity Extension 4 was not initialized!
[ 8768.795828] uvcvideo 1-1.3:1.0: Entity type for entity Extension 3 was not initialized!
[ 8768.795843] uvcvideo 1-1.3:1.0: Entity type for entity Processing 2 was not initialized!
[ 8768.795856] uvcvideo 1-1.3:1.0: Entity type for entity Camera 1 was not initialized!
[ 8768.796612] input: H264 USB Camera: USB Camera as /devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.3/1-1.3:1.0/input/input3
[ 8768.821026] usb 1-1.3: 4:1: cannot get freq at ep 0x84






[ 8902.651896] usb 1-1.3: USB disconnect, device number 4
[ 8908.242120] usb 1-1.4: USB disconnect, device number 3




[ 8916.182188] usb 1-1.4: new high-speed USB device number 5 using xhci_hcd
[ 8916.345744] usb 1-1.4: New USB device found, idVendor=05a3, idProduct=9422, bcdDevice= 1.00
[ 8916.345761] usb 1-1.4: New USB device strings: Mfr=2, Product=1, SerialNumber=3
[ 8916.345773] usb 1-1.4: Product: H264 USB Camera
[ 8916.345785] usb 1-1.4: Manufacturer: Sonix Technology Co., Ltd.
[ 8916.345796] usb 1-1.4: SerialNumber: SN0001
[ 8916.348412] uvcvideo: Found UVC 1.00 device H264 USB Camera (05a3:9422)
[ 8916.386749] uvcvideo: Unable to create debugfs 1-5 directory.
[ 8916.387146] uvcvideo 1-1.4:1.0: Entity type for entity Extension 4 was not initialized!
[ 8916.387162] uvcvideo 1-1.4:1.0: Entity type for entity Extension 3 was not initialized!
[ 8916.387177] uvcvideo 1-1.4:1.0: Entity type for entity Processing 2 was not initialized!
[ 8916.387191] uvcvideo 1-1.4:1.0: Entity type for entity Camera 1 was not initialized!
[ 8916.387532] input: H264 USB Camera: USB Camera as /devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.4/1-1.4:1.0/input/input4
[ 8916.410996] usb 1-1.4: 4:1: cannot get freq at ep 0x84


pi@raspberrypi:~ $ sudo udevadm info -ap /devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.4/1-1.4:1.0/video4linux/video4

Udevadm info starts with the device specified by the devpath and then
walks up the chain of parent devices. It prints for every device
found, all possible attributes in the udev rules key format.
A rule to match, can be composed by the attributes of the device
and the attributes from one single parent device.

  looking at device '//devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.4/1-1.4:1.0/video4linux/video4':
    KERNEL=="video4"
    SUBSYSTEM=="video4linux"
    DRIVER==""
    ATTR{name}=="H264 USB Camera: USB Camera"
    ATTR{dev_debug}=="0"
    ATTR{index}=="3"

  looking at parent device '//devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.4/1-1.4:1.0':
    KERNELS=="1-1.4:1.0"
    SUBSYSTEMS=="usb"
    DRIVERS=="uvcvideo"
    ATTRS{bNumEndpoints}=="01"
    ATTRS{authorized}=="1"
    ATTRS{iad_bFunctionClass}=="0e"
    ATTRS{iad_bFunctionProtocol}=="00"
    ATTRS{iad_bFirstInterface}=="00"
    ATTRS{bInterfaceSubClass}=="01"
    ATTRS{bAlternateSetting}==" 0"
    ATTRS{iad_bFunctionSubClass}=="03"
    ATTRS{bInterfaceNumber}=="00"
    ATTRS{bInterfaceProtocol}=="00"
    ATTRS{bInterfaceClass}=="0e"
    ATTRS{iad_bInterfaceCount}=="03"
    ATTRS{supports_autosuspend}=="1"
    ATTRS{interface}=="USB Camera"

  looking at parent device '//devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.4':
    KERNELS=="1-1.4"
    SUBSYSTEMS=="usb"
    DRIVERS=="usb"
    ATTRS{bConfigurationValue}=="1"
    ATTRS{serial}=="SN0001"
    ATTRS{configuration}==""
    ATTRS{bNumInterfaces}==" 5"
    ATTRS{rx_lanes}=="1"
    ATTRS{bDeviceClass}=="ef"
    ATTRS{speed}=="480"
    ATTRS{maxchild}=="0"
    ATTRS{removable}=="unknown"
    ATTRS{busnum}=="1"
    ATTRS{bcdDevice}=="0100"
    ATTRS{bMaxPower}=="500mA"
    ATTRS{bDeviceSubClass}=="02"
    ATTRS{manufacturer}=="Sonix Technology Co., Ltd."
    ATTRS{devspec}=="  (null)"
    ATTRS{idVendor}=="05a3"
    ATTRS{quirks}=="0x0"
    ATTRS{devpath}=="1.4"
    ATTRS{devnum}=="5"
    ATTRS{idProduct}=="9422"
    ATTRS{authorized}=="1"
    ATTRS{avoid_reset_quirk}=="0"
    ATTRS{urbnum}=="59"
    ATTRS{bDeviceProtocol}=="01"
    ATTRS{bMaxPacketSize0}=="64"
    ATTRS{product}=="H264 USB Camera"
    ATTRS{tx_lanes}=="1"
    ATTRS{bmAttributes}=="80"
    ATTRS{ltm_capable}=="no"
    ATTRS{version}==" 2.00"
    ATTRS{bNumConfigurations}=="1"

  looking at parent device '//devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1':
    KERNELS=="1-1"
    SUBSYSTEMS=="usb"
    DRIVERS=="usb"
    ATTRS{devpath}=="1"
    ATTRS{devnum}=="2"
    ATTRS{configuration}==""
    ATTRS{urbnum}=="116"
    ATTRS{version}==" 2.10"
    ATTRS{bNumConfigurations}=="1"
    ATTRS{removable}=="unknown"
    ATTRS{devspec}=="  (null)"
    ATTRS{bDeviceClass}=="09"
    ATTRS{idVendor}=="2109"
    ATTRS{bDeviceProtocol}=="01"
    ATTRS{bConfigurationValue}=="1"
    ATTRS{maxchild}=="4"
    ATTRS{bMaxPower}=="100mA"
    ATTRS{bMaxPacketSize0}=="64"
    ATTRS{bDeviceSubClass}=="00"
    ATTRS{authorized}=="1"
    ATTRS{bmAttributes}=="e0"
    ATTRS{busnum}=="1"
    ATTRS{tx_lanes}=="1"
    ATTRS{speed}=="480"
    ATTRS{idProduct}=="3431"
    ATTRS{avoid_reset_quirk}=="0"
    ATTRS{product}=="USB2.0 Hub"
    ATTRS{rx_lanes}=="1"
    ATTRS{bcdDevice}=="0420"
    ATTRS{bNumInterfaces}==" 1"
    ATTRS{ltm_capable}=="no"
    ATTRS{quirks}=="0x0"

  looking at parent device '//devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1':
    KERNELS=="usb1"
    SUBSYSTEMS=="usb"
    DRIVERS=="usb"
    ATTRS{interface_authorized_default}=="1"
    ATTRS{speed}=="480"
    ATTRS{bDeviceClass}=="09"
    ATTRS{urbnum}=="66"
    ATTRS{maxchild}=="1"
    ATTRS{avoid_reset_quirk}=="0"
    ATTRS{serial}=="0000:01:00.0"
    ATTRS{rx_lanes}=="1"
    ATTRS{bConfigurationValue}=="1"
    ATTRS{ltm_capable}=="no"
    ATTRS{manufacturer}=="Linux 4.19.66-v7l+ xhci-hcd"
    ATTRS{version}==" 2.00"
    ATTRS{idProduct}=="0002"
    ATTRS{product}=="xHCI Host Controller"
    ATTRS{idVendor}=="1d6b"
    ATTRS{bNumConfigurations}=="1"
    ATTRS{bNumInterfaces}==" 1"
    ATTRS{devnum}=="1"
    ATTRS{removable}=="unknown"
    ATTRS{busnum}=="1"
    ATTRS{devspec}=="  (null)"
    ATTRS{bcdDevice}=="0419"
    ATTRS{authorized_default}=="1"
    ATTRS{bMaxPacketSize0}=="64"
    ATTRS{bmAttributes}=="e0"
    ATTRS{bMaxPower}=="0mA"
    ATTRS{bDeviceSubClass}=="00"
    ATTRS{quirks}=="0x0"
    ATTRS{configuration}==""
    ATTRS{bDeviceProtocol}=="01"
    ATTRS{authorized}=="1"
    ATTRS{tx_lanes}=="1"
    ATTRS{devpath}=="0"

  looking at parent device '//devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0':
    KERNELS=="0000:01:00.0"
    SUBSYSTEMS=="pci"
    DRIVERS=="xhci_hcd"
    ATTRS{local_cpulist}=="0-3"
    ATTRS{current_link_width}=="1"
    ATTRS{driver_override}=="(null)"
    ATTRS{devspec}==""
    ATTRS{device}=="0x3483"
    ATTRS{broken_parity_status}=="0"
    ATTRS{msi_bus}=="1"
    ATTRS{revision}=="0x01"
    ATTRS{vendor}=="0x1106"
    ATTRS{consistent_dma_mask_bits}=="64"
    ATTRS{current_link_speed}=="5 GT/s"
    ATTRS{ari_enabled}=="0"
    ATTRS{max_link_width}=="1"
    ATTRS{subsystem_vendor}=="0x1106"
    ATTRS{enable}=="1"
    ATTRS{max_link_speed}=="5 GT/s"
    ATTRS{local_cpus}=="f"
    ATTRS{irq}=="58"
    ATTRS{dma_mask_bits}=="64"
    ATTRS{class}=="0x0c0330"
    ATTRS{subsystem_device}=="0x3483"

  looking at parent device '//devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0':
    KERNELS=="0000:00:00.0"
    SUBSYSTEMS=="pci"
    DRIVERS=="pcieport"
    ATTRS{irq}=="57"
    ATTRS{device}=="0x2711"
    ATTRS{aer_rootport_total_err_nonfatal}=="0"
    ATTRS{dma_mask_bits}=="32"
    ATTRS{subsystem_vendor}=="0x0000"
    ATTRS{max_link_width}=="1"
    ATTRS{class}=="0x060400"
    ATTRS{ari_enabled}=="0"
    ATTRS{aer_rootport_total_err_fatal}=="0"
    ATTRS{secondary_bus_number}=="1"
    ATTRS{max_link_speed}=="5 GT/s"
    ATTRS{subsystem_device}=="0x0000"
    ATTRS{broken_parity_status}=="0"
    ATTRS{driver_override}=="(null)"
    ATTRS{devspec}==""
    ATTRS{subordinate_bus_number}=="1"
    ATTRS{current_link_speed}=="5 GT/s"
    ATTRS{aer_rootport_total_err_cor}=="0"
    ATTRS{enable}=="1"
    ATTRS{local_cpulist}=="0-3"
    ATTRS{revision}=="0x10"
    ATTRS{current_link_width}=="1"
    ATTRS{vendor}=="0x14e4"
    ATTRS{local_cpus}=="f"
    ATTRS{consistent_dma_mask_bits}=="32"
    ATTRS{msi_bus}=="1"

  looking at parent device '//devices/platform/scb/fd500000.pcie/pci0000:00':
    KERNELS=="pci0000:00"
    SUBSYSTEMS==""
    DRIVERS==""

  looking at parent device '//devices/platform/scb/fd500000.pcie':
    KERNELS=="fd500000.pcie"
    SUBSYSTEMS=="platform"
    DRIVERS=="brcm-pcie"
    ATTRS{driver_override}=="(null)"
    ATTRS{dmabounce_stats}=="m:0/0 s:0/0 f:0 s:0 b:0/0 a:0/0"

  looking at parent device '//devices/platform/scb':
    KERNELS=="scb"
    SUBSYSTEMS=="platform"
    DRIVERS==""
    ATTRS{driver_override}=="(null)"

  looking at parent device '//devices/platform':
    KERNELS=="platform"
    SUBSYSTEMS==""
    DRIVERS==""





[ 8945.933532] usb 1-1.3: new high-speed USB device number 6 using xhci_hcd
[ 8946.107392] usb 1-1.3: New USB device found, idVendor=05a3, idProduct=9422, bcdDevice= 1.00
[ 8946.107409] usb 1-1.3: New USB device strings: Mfr=2, Product=1, SerialNumber=3
[ 8946.107421] usb 1-1.3: Product: H264 USB Camera
[ 8946.107433] usb 1-1.3: Manufacturer: Sonix Technology Co., Ltd.
[ 8946.107450] usb 1-1.3: SerialNumber: SN0001
[ 8946.110136] uvcvideo: Found UVC 1.00 device H264 USB Camera (05a3:9422)
[ 8946.148888] uvcvideo: Unable to create debugfs 1-6 directory.
[ 8946.149313] uvcvideo 1-1.3:1.0: Entity type for entity Extension 4 was not initialized!
[ 8946.149329] uvcvideo 1-1.3:1.0: Entity type for entity Extension 3 was not initialized!
[ 8946.149344] uvcvideo 1-1.3:1.0: Entity type for entity Processing 2 was not initialized!
[ 8946.149358] uvcvideo 1-1.3:1.0: Entity type for entity Camera 1 was not initialized!
[ 8946.149705] input: H264 USB Camera: USB Camera as /devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.3/1-1.3:1.0/input/input5
[ 8946.173069] usb 1-1.3: 4:1: cannot get freq at ep 0x84


pi@raspberrypi:~ $ sudo udevadm info -ap /devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.3/1-1.3:1.0/video4linux/video5

Udevadm info starts with the device specified by the devpath and then
walks up the chain of parent devices. It prints for every device
found, all possible attributes in the udev rules key format.
A rule to match, can be composed by the attributes of the device
and the attributes from one single parent device.

  looking at device '//devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.3/1-1.3:1.0/video4linux/video5':
    KERNEL=="video5"
    SUBSYSTEM=="video4linux"
    DRIVER==""
    ATTR{dev_debug}=="0"
    ATTR{index}=="0"
    ATTR{name}=="H264 USB Camera: USB Camera"

  looking at parent device '//devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.3/1-1.3:1.0':
    KERNELS=="1-1.3:1.0"
    SUBSYSTEMS=="usb"
    DRIVERS=="uvcvideo"
    ATTRS{iad_bFunctionProtocol}=="00"
    ATTRS{iad_bInterfaceCount}=="03"
    ATTRS{iad_bFunctionClass}=="0e"
    ATTRS{iad_bFunctionSubClass}=="03"
    ATTRS{bAlternateSetting}==" 0"
    ATTRS{supports_autosuspend}=="1"
    ATTRS{iad_bFirstInterface}=="00"
    ATTRS{bNumEndpoints}=="01"
    ATTRS{bInterfaceProtocol}=="00"
    ATTRS{bInterfaceNumber}=="00"
    ATTRS{interface}=="USB Camera"
    ATTRS{authorized}=="1"
    ATTRS{bInterfaceSubClass}=="01"
    ATTRS{bInterfaceClass}=="0e"

  looking at parent device '//devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.3':
    KERNELS=="1-1.3"
    SUBSYSTEMS=="usb"
    DRIVERS=="usb"
    ATTRS{devnum}=="6"
    ATTRS{bDeviceClass}=="ef"
    ATTRS{rx_lanes}=="1"
    ATTRS{idVendor}=="05a3"
    ATTRS{bConfigurationValue}=="1"
    ATTRS{product}=="H264 USB Camera"
    ATTRS{bcdDevice}=="0100"
    ATTRS{version}==" 2.00"
    ATTRS{maxchild}=="0"
    ATTRS{speed}=="480"
    ATTRS{bNumConfigurations}=="1"
    ATTRS{bMaxPower}=="500mA"
    ATTRS{serial}=="SN0001"
    ATTRS{authorized}=="1"
    ATTRS{quirks}=="0x0"
    ATTRS{configuration}==""
    ATTRS{busnum}=="1"
    ATTRS{manufacturer}=="Sonix Technology Co., Ltd."
    ATTRS{bmAttributes}=="80"
    ATTRS{avoid_reset_quirk}=="0"
    ATTRS{removable}=="unknown"
    ATTRS{devpath}=="1.3"
    ATTRS{ltm_capable}=="no"
    ATTRS{bDeviceSubClass}=="02"
    ATTRS{urbnum}=="58"
    ATTRS{idProduct}=="9422"
    ATTRS{devspec}=="  (null)"
    ATTRS{bDeviceProtocol}=="01"
    ATTRS{tx_lanes}=="1"
    ATTRS{bNumInterfaces}==" 5"
    ATTRS{bMaxPacketSize0}=="64"

  looking at parent device '//devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1':
    KERNELS=="1-1"
    SUBSYSTEMS=="usb"
    DRIVERS=="usb"
    ATTRS{bmAttributes}=="e0"
    ATTRS{bMaxPacketSize0}=="64"
    ATTRS{removable}=="unknown"
    ATTRS{configuration}==""
    ATTRS{bDeviceProtocol}=="01"
    ATTRS{devpath}=="1"
    ATTRS{ltm_capable}=="no"
    ATTRS{rx_lanes}=="1"
    ATTRS{busnum}=="1"
    ATTRS{quirks}=="0x0"
    ATTRS{bDeviceSubClass}=="00"
    ATTRS{bNumInterfaces}==" 1"
    ATTRS{bConfigurationValue}=="1"
    ATTRS{speed}=="480"
    ATTRS{bNumConfigurations}=="1"
    ATTRS{devspec}=="  (null)"
    ATTRS{idProduct}=="3431"
    ATTRS{tx_lanes}=="1"
    ATTRS{idVendor}=="2109"
    ATTRS{bcdDevice}=="0420"
    ATTRS{product}=="USB2.0 Hub"
    ATTRS{maxchild}=="4"
    ATTRS{urbnum}=="116"
    ATTRS{bMaxPower}=="100mA"
    ATTRS{avoid_reset_quirk}=="0"
    ATTRS{bDeviceClass}=="09"
    ATTRS{version}==" 2.10"
    ATTRS{devnum}=="2"
    ATTRS{authorized}=="1"

  looking at parent device '//devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1':
    KERNELS=="usb1"
    SUBSYSTEMS=="usb"
    DRIVERS=="usb"
    ATTRS{configuration}==""
    ATTRS{maxchild}=="1"
    ATTRS{bcdDevice}=="0419"
    ATTRS{product}=="xHCI Host Controller"
    ATTRS{manufacturer}=="Linux 4.19.66-v7l+ xhci-hcd"
    ATTRS{idVendor}=="1d6b"
    ATTRS{bConfigurationValue}=="1"
    ATTRS{authorized_default}=="1"
    ATTRS{urbnum}=="66"
    ATTRS{bDeviceClass}=="09"
    ATTRS{bMaxPacketSize0}=="64"
    ATTRS{serial}=="0000:01:00.0"
    ATTRS{quirks}=="0x0"
    ATTRS{bNumInterfaces}==" 1"
    ATTRS{tx_lanes}=="1"
    ATTRS{rx_lanes}=="1"
    ATTRS{bNumConfigurations}=="1"
    ATTRS{ltm_capable}=="no"
    ATTRS{authorized}=="1"
    ATTRS{busnum}=="1"
    ATTRS{bMaxPower}=="0mA"
    ATTRS{interface_authorized_default}=="1"
    ATTRS{bDeviceSubClass}=="00"
    ATTRS{bDeviceProtocol}=="01"
    ATTRS{devpath}=="0"
    ATTRS{removable}=="unknown"
    ATTRS{version}==" 2.00"
    ATTRS{speed}=="480"
    ATTRS{avoid_reset_quirk}=="0"
    ATTRS{devspec}=="  (null)"
    ATTRS{idProduct}=="0002"
    ATTRS{bmAttributes}=="e0"
    ATTRS{devnum}=="1"

  looking at parent device '//devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0':
    KERNELS=="0000:01:00.0"
    SUBSYSTEMS=="pci"
    DRIVERS=="xhci_hcd"
    ATTRS{device}=="0x3483"
    ATTRS{subsystem_device}=="0x3483"
    ATTRS{subsystem_vendor}=="0x1106"
    ATTRS{msi_bus}=="1"
    ATTRS{local_cpus}=="f"
    ATTRS{irq}=="58"
    ATTRS{enable}=="1"
    ATTRS{dma_mask_bits}=="64"
    ATTRS{ari_enabled}=="0"
    ATTRS{devspec}==""
    ATTRS{vendor}=="0x1106"
    ATTRS{max_link_width}=="1"
    ATTRS{revision}=="0x01"
    ATTRS{current_link_width}=="1"
    ATTRS{max_link_speed}=="5 GT/s"
    ATTRS{class}=="0x0c0330"
    ATTRS{current_link_speed}=="5 GT/s"
    ATTRS{broken_parity_status}=="0"
    ATTRS{consistent_dma_mask_bits}=="64"
    ATTRS{driver_override}=="(null)"
    ATTRS{local_cpulist}=="0-3"

  looking at parent device '//devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0':
    KERNELS=="0000:00:00.0"
    SUBSYSTEMS=="pci"
    DRIVERS=="pcieport"
    ATTRS{consistent_dma_mask_bits}=="32"
    ATTRS{current_link_width}=="1"
    ATTRS{vendor}=="0x14e4"
    ATTRS{subsystem_device}=="0x0000"
    ATTRS{aer_rootport_total_err_fatal}=="0"
    ATTRS{local_cpulist}=="0-3"
    ATTRS{local_cpus}=="f"
    ATTRS{secondary_bus_number}=="1"
    ATTRS{revision}=="0x10"
    ATTRS{max_link_speed}=="5 GT/s"
    ATTRS{dma_mask_bits}=="32"
    ATTRS{driver_override}=="(null)"
    ATTRS{irq}=="57"
    ATTRS{msi_bus}=="1"
    ATTRS{current_link_speed}=="5 GT/s"
    ATTRS{max_link_width}=="1"
    ATTRS{subordinate_bus_number}=="1"
    ATTRS{broken_parity_status}=="0"
    ATTRS{aer_rootport_total_err_cor}=="0"
    ATTRS{aer_rootport_total_err_nonfatal}=="0"
    ATTRS{class}=="0x060400"
    ATTRS{device}=="0x2711"
    ATTRS{devspec}==""
    ATTRS{enable}=="1"
    ATTRS{ari_enabled}=="0"
    ATTRS{subsystem_vendor}=="0x0000"

  looking at parent device '//devices/platform/scb/fd500000.pcie/pci0000:00':
    KERNELS=="pci0000:00"
    SUBSYSTEMS==""
    DRIVERS==""

  looking at parent device '//devices/platform/scb/fd500000.pcie':
    KERNELS=="fd500000.pcie"
    SUBSYSTEMS=="platform"
    DRIVERS=="brcm-pcie"
    ATTRS{driver_override}=="(null)"
    ATTRS{dmabounce_stats}=="m:0/0 s:0/0 f:0 s:0 b:0/0 a:0/0"

  looking at parent device '//devices/platform/scb':
    KERNELS=="scb"
    SUBSYSTEMS=="platform"
    DRIVERS==""
    ATTRS{driver_override}=="(null)"

  looking at parent device '//devices/platform':
    KERNELS=="platform"
    SUBSYSTEMS==""
    DRIVERS==""





pi@raspberrypi:~ $ sudo udevadm info -ap /devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.3/1-1.3:1.0/video4linux/video6

Udevadm info starts with the device specified by the devpath and then
walks up the chain of parent devices. It prints for every device
found, all possible attributes in the udev rules key format.
A rule to match, can be composed by the attributes of the device
and the attributes from one single parent device.

  looking at device '//devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.3/1-1.3:1.0/video4linux/video6':
    KERNEL=="video6"
    SUBSYSTEM=="video4linux"
    DRIVER==""
    ATTR{name}=="H264 USB Camera: USB Camera"
    ATTR{index}=="1"
    ATTR{dev_debug}=="0"

  looking at parent device '//devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.3/1-1.3:1.0':
    KERNELS=="1-1.3:1.0"
    SUBSYSTEMS=="usb"
    DRIVERS=="uvcvideo"
    ATTRS{bInterfaceNumber}=="00"
    ATTRS{bAlternateSetting}==" 0"
    ATTRS{supports_autosuspend}=="1"
    ATTRS{bInterfaceSubClass}=="01"
    ATTRS{bNumEndpoints}=="01"
    ATTRS{iad_bInterfaceCount}=="03"
    ATTRS{bInterfaceClass}=="0e"
    ATTRS{interface}=="USB Camera"
    ATTRS{iad_bFunctionSubClass}=="03"
    ATTRS{iad_bFunctionProtocol}=="00"
    ATTRS{bInterfaceProtocol}=="00"
    ATTRS{iad_bFirstInterface}=="00"
    ATTRS{iad_bFunctionClass}=="0e"
    ATTRS{authorized}=="1"

  looking at parent device '//devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.3':
    KERNELS=="1-1.3"
    SUBSYSTEMS=="usb"
    DRIVERS=="usb"
    ATTRS{rx_lanes}=="1"
    ATTRS{bDeviceProtocol}=="01"
    ATTRS{bmAttributes}=="80"
    ATTRS{ltm_capable}=="no"
    ATTRS{busnum}=="1"
    ATTRS{idVendor}=="05a3"
    ATTRS{configuration}==""
    ATTRS{bNumConfigurations}=="1"
    ATTRS{bcdDevice}=="0100"
    ATTRS{speed}=="480"
    ATTRS{bMaxPacketSize0}=="64"
    ATTRS{product}=="H264 USB Camera"
    ATTRS{removable}=="unknown"
    ATTRS{devpath}=="1.3"
    ATTRS{idProduct}=="9422"
    ATTRS{devnum}=="7"
    ATTRS{authorized}=="1"
    ATTRS{devspec}=="  (null)"
    ATTRS{bMaxPower}=="500mA"
    ATTRS{bDeviceClass}=="ef"
    ATTRS{maxchild}=="0"
    ATTRS{bConfigurationValue}=="1"
    ATTRS{serial}=="SN0001"
    ATTRS{bNumInterfaces}==" 5"
    ATTRS{manufacturer}=="Sonix Technology Co., Ltd."
    ATTRS{version}==" 2.00"
    ATTRS{tx_lanes}=="1"
    ATTRS{avoid_reset_quirk}=="0"
    ATTRS{urbnum}=="60"
    ATTRS{bDeviceSubClass}=="02"
    ATTRS{quirks}=="0x0"

  looking at parent device '//devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1':
    KERNELS=="1-1"
    SUBSYSTEMS=="usb"
    DRIVERS=="usb"
    ATTRS{devspec}=="  (null)"
    ATTRS{bDeviceProtocol}=="01"
    ATTRS{tx_lanes}=="1"
    ATTRS{urbnum}=="145"
    ATTRS{rx_lanes}=="1"
    ATTRS{devnum}=="2"
    ATTRS{authorized}=="1"
    ATTRS{bmAttributes}=="e0"
    ATTRS{idVendor}=="2109"
    ATTRS{bMaxPacketSize0}=="64"
    ATTRS{bMaxPower}=="100mA"
    ATTRS{bDeviceSubClass}=="00"
    ATTRS{bcdDevice}=="0420"
    ATTRS{bNumInterfaces}==" 1"
    ATTRS{maxchild}=="4"
    ATTRS{devpath}=="1"
    ATTRS{busnum}=="1"
    ATTRS{quirks}=="0x0"
    ATTRS{product}=="USB2.0 Hub"
    ATTRS{version}==" 2.10"
    ATTRS{removable}=="unknown"
    ATTRS{bConfigurationValue}=="1"
    ATTRS{ltm_capable}=="no"
    ATTRS{speed}=="480"
    ATTRS{idProduct}=="3431"
    ATTRS{avoid_reset_quirk}=="0"
    ATTRS{configuration}==""
    ATTRS{bDeviceClass}=="09"
    ATTRS{bNumConfigurations}=="1"

  looking at parent device '//devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1':
    KERNELS=="usb1"
    SUBSYSTEMS=="usb"
    DRIVERS=="usb"
    ATTRS{devpath}=="0"
    ATTRS{bNumConfigurations}=="1"
    ATTRS{idVendor}=="1d6b"
    ATTRS{authorized_default}=="1"
    ATTRS{devnum}=="1"
    ATTRS{removable}=="unknown"
    ATTRS{quirks}=="0x0"
    ATTRS{bDeviceSubClass}=="00"
    ATTRS{tx_lanes}=="1"
    ATTRS{product}=="xHCI Host Controller"
    ATTRS{speed}=="480"
    ATTRS{interface_authorized_default}=="1"
    ATTRS{bMaxPower}=="0mA"
    ATTRS{urbnum}=="80"
    ATTRS{manufacturer}=="Linux 4.19.66-v7l+ xhci-hcd"
    ATTRS{avoid_reset_quirk}=="0"
    ATTRS{configuration}==""
    ATTRS{bMaxPacketSize0}=="64"
    ATTRS{bcdDevice}=="0419"
    ATTRS{serial}=="0000:01:00.0"
    ATTRS{rx_lanes}=="1"
    ATTRS{devspec}=="  (null)"
    ATTRS{busnum}=="1"
    ATTRS{idProduct}=="0002"
    ATTRS{version}==" 2.00"
    ATTRS{bConfigurationValue}=="1"
    ATTRS{bDeviceClass}=="09"
    ATTRS{bmAttributes}=="e0"
    ATTRS{ltm_capable}=="no"
    ATTRS{maxchild}=="1"
    ATTRS{authorized}=="1"
    ATTRS{bNumInterfaces}==" 1"
    ATTRS{bDeviceProtocol}=="01"

  looking at parent device '//devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0':
    KERNELS=="0000:01:00.0"
    SUBSYSTEMS=="pci"
    DRIVERS=="xhci_hcd"
    ATTRS{msi_bus}=="1"
    ATTRS{dma_mask_bits}=="64"
    ATTRS{subsystem_device}=="0x3483"
    ATTRS{vendor}=="0x1106"
    ATTRS{local_cpus}=="f"
    ATTRS{max_link_width}=="1"
    ATTRS{revision}=="0x01"
    ATTRS{local_cpulist}=="0-3"
    ATTRS{subsystem_vendor}=="0x1106"
    ATTRS{driver_override}=="(null)"
    ATTRS{device}=="0x3483"
    ATTRS{consistent_dma_mask_bits}=="64"
    ATTRS{max_link_speed}=="5 GT/s"
    ATTRS{class}=="0x0c0330"
    ATTRS{enable}=="1"
    ATTRS{devspec}==""
    ATTRS{ari_enabled}=="0"
    ATTRS{irq}=="58"
    ATTRS{broken_parity_status}=="0"
    ATTRS{current_link_width}=="1"
    ATTRS{current_link_speed}=="5 GT/s"

  looking at parent device '//devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0':
    KERNELS=="0000:00:00.0"
    SUBSYSTEMS=="pci"
    DRIVERS=="pcieport"
    ATTRS{subsystem_vendor}=="0x0000"
    ATTRS{local_cpus}=="f"
    ATTRS{ari_enabled}=="0"
    ATTRS{devspec}==""
    ATTRS{dma_mask_bits}=="32"
    ATTRS{max_link_speed}=="5 GT/s"
    ATTRS{irq}=="57"
    ATTRS{max_link_width}=="1"
    ATTRS{enable}=="1"
    ATTRS{aer_rootport_total_err_nonfatal}=="0"
    ATTRS{revision}=="0x10"
    ATTRS{local_cpulist}=="0-3"
    ATTRS{broken_parity_status}=="0"
    ATTRS{current_link_speed}=="5 GT/s"
    ATTRS{class}=="0x060400"
    ATTRS{aer_rootport_total_err_fatal}=="0"
    ATTRS{msi_bus}=="1"
    ATTRS{device}=="0x2711"
    ATTRS{vendor}=="0x14e4"
    ATTRS{subordinate_bus_number}=="1"
    ATTRS{aer_rootport_total_err_cor}=="0"
    ATTRS{subsystem_device}=="0x0000"
    ATTRS{consistent_dma_mask_bits}=="32"
    ATTRS{driver_override}=="(null)"
    ATTRS{current_link_width}=="1"
    ATTRS{secondary_bus_number}=="1"

  looking at parent device '//devices/platform/scb/fd500000.pcie/pci0000:00':
    KERNELS=="pci0000:00"
    SUBSYSTEMS==""
    DRIVERS==""

  looking at parent device '//devices/platform/scb/fd500000.pcie':
    KERNELS=="fd500000.pcie"
    SUBSYSTEMS=="platform"
    DRIVERS=="brcm-pcie"
    ATTRS{dmabounce_stats}=="m:0/0 s:0/0 f:0 s:0 b:0/0 a:0/0"
    ATTRS{driver_override}=="(null)"

  looking at parent device '//devices/platform/scb':
    KERNELS=="scb"
    SUBSYSTEMS=="platform"
    DRIVERS==""
    ATTRS{driver_override}=="(null)"

  looking at parent device '//devices/platform':
    KERNELS=="platform"
    SUBSYSTEMS==""
    DRIVERS==""


pi@raspberrypi:~ $ sudo udevadm info -ap /devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.1/1-1.1:1.0/video4linux/video2

Udevadm info starts with the device specified by the devpath and then
walks up the chain of parent devices. It prints for every device
found, all possible attributes in the udev rules key format.
A rule to match, can be composed by the attributes of the device
and the attributes from one single parent device.

  looking at device '//devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.1/1-1.1:1.0/video4linux/video2':
    KERNEL=="video2"
    SUBSYSTEM=="video4linux"
    DRIVER==""
    ATTR{index}=="1"
    ATTR{name}=="H264 USB Camera: USB Camera"
    ATTR{dev_debug}=="0"

  looking at parent device '//devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.1/1-1.1:1.0':
    KERNELS=="1-1.1:1.0"
    SUBSYSTEMS=="usb"
    DRIVERS=="uvcvideo"
    ATTRS{iad_bFunctionProtocol}=="00"
    ATTRS{iad_bInterfaceCount}=="03"
    ATTRS{iad_bFunctionSubClass}=="03"
    ATTRS{authorized}=="1"
    ATTRS{iad_bFirstInterface}=="00"
    ATTRS{bInterfaceProtocol}=="00"
    ATTRS{bInterfaceClass}=="0e"
    ATTRS{supports_autosuspend}=="1"
    ATTRS{iad_bFunctionClass}=="0e"
    ATTRS{bInterfaceSubClass}=="01"
    ATTRS{bInterfaceNumber}=="00"
    ATTRS{interface}=="USB Camera"
    ATTRS{bAlternateSetting}==" 0"
    ATTRS{bNumEndpoints}=="01"

  looking at parent device '//devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.1':
    KERNELS=="1-1.1"
    SUBSYSTEMS=="usb"
    DRIVERS=="usb"
    ATTRS{urbnum}=="59"
    ATTRS{maxchild}=="0"
    ATTRS{bDeviceSubClass}=="02"
    ATTRS{speed}=="480"
    ATTRS{bmAttributes}=="80"
    ATTRS{serial}=="SN0001"
    ATTRS{quirks}=="0x0"
    ATTRS{bNumConfigurations}=="1"
    ATTRS{manufacturer}=="Sonix Technology Co., Ltd."
    ATTRS{bcdDevice}=="0100"
    ATTRS{configuration}==""
    ATTRS{bConfigurationValue}=="1"
    ATTRS{devpath}=="1.1"
    ATTRS{bMaxPower}=="500mA"
    ATTRS{tx_lanes}=="1"
    ATTRS{product}=="H264 USB Camera"
    ATTRS{version}==" 2.00"
    ATTRS{bNumInterfaces}==" 5"
    ATTRS{idProduct}=="9422"
    ATTRS{authorized}=="1"
    ATTRS{devspec}=="  (null)"
    ATTRS{bMaxPacketSize0}=="64"
    ATTRS{avoid_reset_quirk}=="0"
    ATTRS{bDeviceProtocol}=="01"
    ATTRS{devnum}=="15"
    ATTRS{idVendor}=="05a3"
    ATTRS{busnum}=="1"
    ATTRS{bDeviceClass}=="ef"
    ATTRS{removable}=="unknown"
    ATTRS{ltm_capable}=="no"
    ATTRS{rx_lanes}=="1"

  looking at parent device '//devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1':
    KERNELS=="1-1"
    SUBSYSTEMS=="usb"
    DRIVERS=="usb"
    ATTRS{bDeviceProtocol}=="01"
    ATTRS{avoid_reset_quirk}=="0"
    ATTRS{removable}=="unknown"
    ATTRS{idProduct}=="3431"
    ATTRS{tx_lanes}=="1"
    ATTRS{urbnum}=="388"
    ATTRS{bMaxPacketSize0}=="64"
    ATTRS{product}=="USB2.0 Hub"
    ATTRS{ltm_capable}=="no"
    ATTRS{authorized}=="1"
    ATTRS{speed}=="480"
    ATTRS{idVendor}=="2109"
    ATTRS{bcdDevice}=="0420"
    ATTRS{bNumConfigurations}=="1"
    ATTRS{configuration}==""
    ATTRS{bMaxPower}=="100mA"
    ATTRS{devnum}=="2"
    ATTRS{bNumInterfaces}==" 1"
    ATTRS{version}==" 2.10"
    ATTRS{rx_lanes}=="1"
    ATTRS{bConfigurationValue}=="1"
    ATTRS{maxchild}=="4"
    ATTRS{bDeviceSubClass}=="00"
    ATTRS{devspec}=="  (null)"
    ATTRS{devpath}=="1"
    ATTRS{busnum}=="1"
    ATTRS{bDeviceClass}=="09"
    ATTRS{quirks}=="0x0"
    ATTRS{bmAttributes}=="e0"

  looking at parent device '//devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1':
    KERNELS=="usb1"
    SUBSYSTEMS=="usb"
    DRIVERS=="usb"
    ATTRS{tx_lanes}=="1"
    ATTRS{version}==" 2.00"
    ATTRS{idProduct}=="0002"
    ATTRS{ltm_capable}=="no"
    ATTRS{bcdDevice}=="0419"
    ATTRS{devspec}=="  (null)"
    ATTRS{bNumInterfaces}==" 1"
    ATTRS{quirks}=="0x0"
    ATTRS{bDeviceProtocol}=="01"
    ATTRS{configuration}==""
    ATTRS{removable}=="unknown"
    ATTRS{rx_lanes}=="1"
    ATTRS{bMaxPacketSize0}=="64"
    ATTRS{busnum}=="1"
    ATTRS{speed}=="480"
    ATTRS{interface_authorized_default}=="1"
    ATTRS{bMaxPower}=="0mA"
    ATTRS{authorized_default}=="1"
    ATTRS{devnum}=="1"
    ATTRS{bNumConfigurations}=="1"
    ATTRS{manufacturer}=="Linux 4.19.66-v7l+ xhci-hcd"
    ATTRS{serial}=="0000:01:00.0"
    ATTRS{idVendor}=="1d6b"
    ATTRS{bmAttributes}=="e0"
    ATTRS{bConfigurationValue}=="1"
    ATTRS{devpath}=="0"
    ATTRS{urbnum}=="199"
    ATTRS{product}=="xHCI Host Controller"
    ATTRS{bDeviceClass}=="09"
    ATTRS{authorized}=="1"
    ATTRS{avoid_reset_quirk}=="0"
    ATTRS{bDeviceSubClass}=="00"
    ATTRS{maxchild}=="1"

  looking at parent device '//devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0':
    KERNELS=="0000:01:00.0"
    SUBSYSTEMS=="pci"
    DRIVERS=="xhci_hcd"
    ATTRS{driver_override}=="(null)"
    ATTRS{current_link_speed}=="5 GT/s"
    ATTRS{current_link_width}=="1"
    ATTRS{local_cpulist}=="0-3"
    ATTRS{device}=="0x3483"
    ATTRS{max_link_width}=="1"
    ATTRS{subsystem_device}=="0x3483"
    ATTRS{enable}=="1"
    ATTRS{consistent_dma_mask_bits}=="64"
    ATTRS{local_cpus}=="f"
    ATTRS{msi_bus}=="1"
    ATTRS{irq}=="58"
    ATTRS{vendor}=="0x1106"
    ATTRS{broken_parity_status}=="0"
    ATTRS{devspec}==""
    ATTRS{class}=="0x0c0330"
    ATTRS{dma_mask_bits}=="64"
    ATTRS{subsystem_vendor}=="0x1106"
    ATTRS{ari_enabled}=="0"
    ATTRS{max_link_speed}=="5 GT/s"
    ATTRS{revision}=="0x01"

  looking at parent device '//devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0':
    KERNELS=="0000:00:00.0"
    SUBSYSTEMS=="pci"
    DRIVERS=="pcieport"
    ATTRS{enable}=="1"
    ATTRS{ari_enabled}=="0"
    ATTRS{subsystem_vendor}=="0x0000"
    ATTRS{vendor}=="0x14e4"
    ATTRS{aer_rootport_total_err_cor}=="0"
    ATTRS{driver_override}=="(null)"
    ATTRS{local_cpus}=="f"
    ATTRS{msi_bus}=="1"
    ATTRS{device}=="0x2711"
    ATTRS{subordinate_bus_number}=="1"
    ATTRS{local_cpulist}=="0-3"
    ATTRS{aer_rootport_total_err_nonfatal}=="0"
    ATTRS{irq}=="57"
    ATTRS{consistent_dma_mask_bits}=="32"
    ATTRS{max_link_width}=="1"
    ATTRS{subsystem_device}=="0x0000"
    ATTRS{current_link_speed}=="5 GT/s"
    ATTRS{dma_mask_bits}=="32"
    ATTRS{max_link_speed}=="5 GT/s"
    ATTRS{secondary_bus_number}=="1"
    ATTRS{revision}=="0x10"
    ATTRS{aer_rootport_total_err_fatal}=="0"
    ATTRS{class}=="0x060400"
    ATTRS{devspec}==""
    ATTRS{broken_parity_status}=="0"
    ATTRS{current_link_width}=="1"

  looking at parent device '//devices/platform/scb/fd500000.pcie/pci0000:00':
    KERNELS=="pci0000:00"
    SUBSYSTEMS==""
    DRIVERS==""

  looking at parent device '//devices/platform/scb/fd500000.pcie':
    KERNELS=="fd500000.pcie"
    SUBSYSTEMS=="platform"
    DRIVERS=="brcm-pcie"
    ATTRS{driver_override}=="(null)"
    ATTRS{dmabounce_stats}=="m:0/0 s:0/0 f:0 s:0 b:0/0 a:0/0"

  looking at parent device '//devices/platform/scb':
    KERNELS=="scb"
    SUBSYSTEMS=="platform"
    DRIVERS==""
    ATTRS{driver_override}=="(null)"

  looking at parent device '//devices/platform':
    KERNELS=="platform"
    SUBSYSTEMS==""
    DRIVERS==""
