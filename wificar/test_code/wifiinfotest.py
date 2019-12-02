#from pythonwifi.iwlibs import Wireless
#import pythonwifi
#wifi = Wireless("wlp2s0")
#print(wifi.getEssid())
#print(wifi.getMode())
#print(wifi.get_frequency())
#print(wifi.get_tx_power())

#print(wifi.get_bitrates())

import subprocess

results = subprocess.check_output(["iwconfig"])
results = results.decode("ascii")
results = results.replace("\r","")
results = results.replace("\n","")
results = results.replace("   "," ")
results = results.replace("  "," ")
ls = results.split(" ")
x=0
while x < len(ls):
    ls[x] = ls[x].strip()
    print(ls[x])
    x += 1
#print(ls)

ls = ls[4:]
ssids = []
x = 0
while x < len(ls):
    if x % 5 == 0:
        ssids.append(ls[x])
    x += 1
print(ssids)