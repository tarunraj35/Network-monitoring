from pcapfile import savefile
from pcapfile.protocols.linklayer import ethernet
from pcapfile.protocols.network import ip
import binascii

rest_ip = "192.168.1.7"
testcap = open('black_list.pcap','rb')

capfile = savefile.load_savefile(testcap,layers=2,verbose = True)
print(len(capfile.packets))
ip = capfile.packets[0].packet.payload
ip = str(ip)


for i in range(len(capfile.packets)):
    ip = str(capfile.packets[i].packet.payload)
    if rest_ip in ip:
        print(ip[19:31])



