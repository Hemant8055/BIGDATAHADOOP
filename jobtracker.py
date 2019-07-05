#!/usr/bin/python36

print("content-type: text\html")
import subprocess as sp
import os
import cgi

form=cgi.FieldStorage()
ip_j=form.getvalue('ip_j')
ip=form.getvalue('ip_m')
user=form.getvalue('usr_j')
passwd=form.getvalue('pass_j')
job=open('/var/www/cgi-bin/hadoop/mapred-site.xml','w')
job.write(
"""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>mapred.job.tracker</name>
<value>{}:9002</value>
</property>
</configuration>
""".format(ip_j))
job.close()	

job=open('/var/www/cgi-bin/hadoop/core-site.xml','w')
job.write(
"""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:9002</value>
</property>
</configuration>""".format(ip))
job.close()
sp.getoutput("sshpass -p {} scp -o StrictHostKeyChecking=no /var/www/cgi-bin/hadoop/mapred-site.xml {}@{}:/etc/hadoop".format(passwd,user,ip_j))	
sp.getoutput("sshpass -p {} scp -o StrictHostKeyChecking=no /var/www/cgi-bin/hadoop/core-site.xml {}@{}:/etc/hadoop".format(passwd,user,ip_j))	
sp.getoutput("sshpass -p {} ssh -l {} {} 'iptables -F'".format(passwd,user,ip_j))
sp.getoutput("sshpass -p {} ssh -l {} {} 'hadoop-daemon.sh start jobtracker'".format(passwd,user,ip_j))
jps_check=sp.getoutput("sshpass -p {} ssh -l {} {} 'jps|grep jobtracker'".format(passwd,user,ip_j))
if jps_check!=' ':
	print("location:mapred.py")
	print("")
else:
	print("")
	print("not installed")
