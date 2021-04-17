import nmap3
import os
import netifaces as ni
import schedule
import time


def check_ping(ip):
    hostname = ip
    response = os.system("ping -c 1 " + ip)
    # and then check the response...
    if response == 0:
        pingstatus = ip + " Host Active"
    else:
        pingstatus = ip + " Host Down"

    print(pingstatus)


nmap = nmap3.Nmap()
ni.ifaddresses('eno1')
ip = ni.ifaddresses('eno1')[ni.AF_INET][0]['addr']
results = nmap.scan_top_ports(ip, args="-sn")

ip = list(results.keys())


def func():
    for i in ip:
        check_ping(i)

schedule.every(1).minutes.do(func)

while True:
    schedule.run_pending()
    time.sleep(1)

