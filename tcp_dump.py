import shlex, subprocess

command = "tcpdump -c 10 -w black_list.pcap -i eno1 dst 192.168.1.7"

args = shlex.split(command)

subprocess.Popen(args)

