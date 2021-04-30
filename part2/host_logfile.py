
import os

# Verifies your os type
OS_TYPE = os.name
# Sets the count modifier to the os type
count = '-n' if OS_TYPE == 'nt' else '-c'

def create_ip_list():
    ip_list = []
    with open("ip.txt", "r") as file:
        for line in file:
            ip_list.append(line.strip())
    return ip_list


def ping_device(ip_list):
    results_file = open("results.txt", "w")
    for ip in ip_list:
        response = os.system("ping -c 1 " + ip)
        if response == 0:
            print(f"UP {ip} Ping Successful")
            results_file.write(f"UP {ip} Ping Successful" + "\n")
        else:
            print(f"Down {ip} Ping Unsuccessful")
            results_file.write(f"Down {ip} Ping Unsuccessful" + "\n")
    results_file.close()


if __name__ == "__main__":
    ping_device(create_ip_list())
