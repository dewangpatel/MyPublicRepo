import os
import netmiko
import datetime
import re

os.chdir('C:\\temp')
os.getcwd()

n = str(datetime.datetime.now())

uname = os.environ['uname']
pwd = os.environ['pwd']

connection=netmiko.ConnectHandler(ip="192.168.2.58", device_type="cisco_ios", username=os.environ['uname'], password=os.environ['pwd'], secret=os.environ['pwd'])

connection.enable()
Line="*=******++++++==============**=*=*"

text_file = open("C:\\temp\Router.txt", "a+")

#text_file.write(connection.send_command("show run inter gi0/1"))

#connection.send_command("show run inter gi0/0")
# To_Execute = connection.send_command("show ip int brief")
# print(To_Execute)

### 
List_of_Commands = ["int gi0/1", "shut", "end"]
To_Execute = connection.send_config_set(List_of_Commands)
print(To_Execute)
text_file.write("@=== "+ n)
text_file.write('\n')
text_file.write(connection.send_command("show run inter gi0/1"))

### 
List_of_Commands = ["int gi0/1", "no shut", "end"]
To_Execute = connection.send_config_set(List_of_Commands)
print(To_Execute)
text_file.write("@=== "+ n)
text_file.write('\n')
text_file.write(connection.send_command("show run inter gi0/1"))
###

regex = r"\d*.bits/sec"

test_str = connection.send_command("show interfaces gigabitEthernet 0/0 | include 5 min")
input_rate = re.findall(regex,test_str)[0][:-9]
output_rate= re.findall(regex,test_str)[1][:-9]
print(input_rate)
print(output_rate)

text_file1 = open("C:\\temp\Router1.txt", "w+")
text_file1.write(connection.send_command("show run"))

text_file1.close()
with open('Router1.txt', "r") as textfile1:
	textlines = textfile1.read().splitlines()

text_to_find = 'version 15.7'

if text_to_find in textlines:
    print("yes "+ text_to_find +" exists")
else:
    print(text_to_find +" does not exists")
	


text_file.close()
connection.disconnect()
