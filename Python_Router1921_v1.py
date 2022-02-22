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

regex = r"\d*.bits/sec"

test_str = connection.send_command("show interfaces gigabitEthernet 0/0 | include 5 min")
input_rate = re.findall(regex,test_str)[0][:-9]
output_rate= re.findall(regex,test_str)[1][:-9]
print(input_rate)
print(output_rate)

text_file = open("C:\\temp\Router3.txt", "w+")
text_file.write(connection.send_command("show run"))

text_file.close()
with open('Router3.txt', "r") as textfile1:
	textlines = textfile1.read().splitlines()

text_to_find = 'line con 0'

if text_to_find in textlines:
    print("yes "+ text_to_find +" exists")
else:
    print(text_to_find +" does not exists")
	


text_file.close()
connection.disconnect()
