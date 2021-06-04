import shlex,subprocess
command = "iptables -F"
args = shlex.split(command)
subprocess.Popen(args)


command = "sudo iptables -A FORWARD -d 192.168.1.7 -j DROP"
args = shlex.split(command)
subprocess.Popen(args)
