import socket
import sys
from datetime import datetime

file = open("Port - Scanner.txt", "w")
  
    
host = input("Please Enter host to Scan: ")
host = "localhost"
host_ip = socket.gethostbyname(host)
file.write("\nScanning Host: {}\n".format(host_ip))

t1 = datetime.now()
print("Start Time: {}".format(t1))    
file.write("Start Time: {}\n".format(t1))
print("Finding Open Ports: In-Progress..........")

for port in range(1, 1025):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.001)
    result = sock.connect_ex((host_ip, port))
    if result == 0:
        print("port {} is Open".format(port))
        file.write("\nport {} is Open".format(port))
    #else:
       # print("port {} is Close".format(port))
        
print("HostName you Entered is not correct")
sys.exit()
    
    
print("Couldn't connect to Server") 
sys.exit()
t2 = datetime.now()
print("End Time: {}".format(t2))  
file.write("\n\nEnd Time: {}".format(t2))

total_time = t2 - t1
print("total Time: {}".format(total_time))  
file.write("\n\ntotal Time: {}".format(total_time))


print(host)
print(host_ip)






