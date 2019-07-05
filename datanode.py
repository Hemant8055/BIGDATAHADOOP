#!/usr/bin/python36

print("content-type:text\html")	

import subprocess as sp
import cgi

form=cgi.FieldStorage()
ip_s=form.getvalue('ip_s')
ip=form.getvalue('ip_m')
user=form.getvalue('usr_s')
passwd=form.getvalue('pass_s')
dir_s=form.getvalue('dir_s')
slave=open('/var/www/cgi-bin/hadoop/hdfs-site.xml','w')
slave.write(
"""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.data.dir</name>
<value>/{}</value>
</property>
</configuration>""".format(dir_s))
slave.close()	
slave=open('/var/www/cgi-bin/hadoop/core-site.xml','w')
slave.write(
"""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:9001</value>
</property>
</configuration>""".format(ip))
slave.close()
sp.getoutput("sshpass -p {} scp -o StrictHostKeyChecking=no /var/www/cgi-bin/hadoop/hdfs-site.xml {}@{}:/etc/hadoop".format(passwd,user,ip_s))	
sp.getoutput("sshpass -p {} scp -o StrictHostKeyChecking=no /var/www/cgi-bin/hadoop/core-site.xml {}@{}:/etc/hadoop".format(passwd,user,ip_s))	
sp.getoutput("sshpass -p {} ssh -l {} {} 'iptables -F'".format(passwd,user,ip_s))
sp.getoutput("sshpass -p {} ssh -l {} {} 'hadoop-daemon.sh start datanode'".format(passwd,user,ip_s))
jps_check=sp.getoutput("sshpass -p {} ssh -l {} {} 'jps|grep DataNode'".format(passwd,user,ip_s))
if jps_check!=' ':
	print("location:auto.py")
	print("")
else:
	print("")
	print("not installed")
