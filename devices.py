import nmap3
import os
def check_ping(ip):
    hostname = ip
    response = os.system("ping -c 1 " + ip)
    # and then check the response...
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"

    print(pingstatus)
nmap = nmap3.Nmap()
results = nmap.scan_top_ports("192.168.1.0/24", args="-sn")

ip = list(results.keys())
for i in ip:
    check_ping(i)
