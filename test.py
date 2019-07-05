import subprocess
import os

#subprocess.getoutput("sshpass -p redhat ssh -o StrictHostKeyChecking=no -l root 192.168.43.229;scp -r /nn root@192.163.43.36:/") 
while True:		
	y=subprocess.getoutput("nmap -sP 192.168.43.0/24 | grep 192.168.43.")
	if ("192.168.43.229" not in y):
		break;

subprocess.getoutput("cp ~/Desktop/cnf.txt /etc/sysconfig/network-scripts/ifcfg-enp0s3")
subprocess.getoutput("systemctl restart network")
subprocess.getoutput("iptables -F")
subprocess.getoutput("hadoop-daemon.sh start namenode")
x=subprocess.getoutput("jps")
if ("NameNode" in x)==True:
 print("created")
else:
 print("not created")

