import nmap 

nm = nmap.PortScanner()

s_range = nm.scan(hosts="192.168.1.9")

print(s_range['scan'])
