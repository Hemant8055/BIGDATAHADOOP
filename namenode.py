#!/usr/bin/python36

print("content-type: text\html")	
import subprocess as sp
import os
import cgi

form=cgi.FieldStorage()
ip=form.getvalue('ip_m')
user=form.getvalue('usr_m')
passwd=form.getvalue('pass_m')
dir_m=form.getvalue('dir_m')
master=open('/var/www/cgi-bin/hadoop/hdfs-site.xml','w')
master.write(
"""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.name.dir</name>
<value>/{}</value>
</property>
</configuration>""".format(dir_m))
master.close()	

master=open('/var/www/cgi-bin/hadoop/core-site.xml','w')
master.write(
"""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:9001</value>
</property>
</configuration>""".format(ip))
master.close()
sp.getoutput("sshpass -p {} scp -o StrictHostKeyChecking=no /var/www/cgi-bin/hadoop/hdfs-site.xml {}@{}:/etc/hadoop".format(passwd,user,ip))	
sp.getoutput("sshpass -p {} scp -o StrictHostKeyChecking=no /var/www/cgi-bin/hadoop/core-site.xml {}@{}:/etc/hadoop".format(passwd,user,ip))	
sp.getoutput("sshpass -p {} ssh -l {} {} 'echo Y | hadoop namenode -format'".format(passwd,user,ip))
sp.getoutput("sshpass -p {} ssh -l {} {} 'iptables -F'".format(passwd,user,ip))
sp.getoutput("sshpass -p {} ssh -l {} {} 'hadoop-daemon.sh start namenode'".format(passwd,user,ip))
jps_check=sp.getoutput("sshpass -p {} ssh -l {} {} 'jps|grep NameNode'".format(passwd,user,ip))
if jps_check!=' ':
	print("location:auto.py")
	print("")
else:
	print("")
	print("not installed")
