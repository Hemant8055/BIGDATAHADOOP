#!/usr/bin/python36

print("content-type:text/html")
print("")

print("<marquee><h1>MAP REDUCE CLUSTER<h1></marquee>")
print("""
<form action=jobtracker.py>
<b>JOB TRACKER</b>
<table border=1>
	<tr>
	<td>Enter JobTracker IP</td>
	<td><input name='ip_j'/></td>
	</tr>
	<tr>
	<td>Enter Masters IP</td>
	<td><input name='ip_m'/></td>
	</tr>
	<tr>
	<td>Enter username</td>
	<td><input name='usr_j'/></td>
	</tr>
	<tr>
	<td>Enter password</td>
	<td><input name='pass_j'/></td>
	</tr>
	<tr>
	<td></td>
	<td><input type=submit value="Submit" /></td>
	</tr>
</table>
</form>""")
print("""

<br/>
<form action=tasktracker.py>
<b>TASK TRACKER</b>
<table border=1>
	<tr>
	<td>Enter IP</td>
	<td><input name='ip_s'/></td>
	</tr>
	<tr>
	<td>Enter NameNode IP</td>
	<td><input name='ip_m'/></td>
	</tr>
	<tr>
	<td>Enter username</td>
	<td><input name='usr_s'/></td>
	</tr>
	<tr>
	<td>Enter password</td>
	<td><input name='pass_s'/></td>
	</tr>
	<tr>
	<td>Enter Directory</td>
	<td><input name='dir_s'/></td>
	</tr>
	<tr>
	<td></td>
	<td><input type=submit value="Submit"/></td>
	</tr>
</table>
</form>""")
