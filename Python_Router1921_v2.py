import os
import netmiko
import datetime
import re
import pandas as pd

os.chdir('C:\\temp')
os.getcwd()

n = str(datetime.datetime.now())
column_names = ["Neighbor","V", "AS", "MRcvd", "Msent", "TblVer", "In", "Out", "UPDown", "StatePfxRcd"]
df = pd.DataFrame(columns = column_names)


with open('bgp.txt', "r") as textfile:
    textlines = textfile.read().splitlines()

text_to_find = 'line con 0'

textfile = open("bgp1.txt", "w")

b=0
for a in range(len(textlines)):
    if ("Neighbor" in textlines[b]):
        print("yes")
        print(b)
        c=b+1
        #textfile.write(textlines[b]+"\n")
    b+=1
    


print("value of c",c)
for x in range (c, len(textlines)):
    textfile.write(textlines[c]+"\n")
    print(textlines[c])
    print(x,c)
    c+=1
textfile.close()
df = pd.read_csv("bgp1.txt", delimiter=r"\s+",names=column_names)
df.to_csv("bgp.csv")

df.StatePfxRcd.isin([0,1,2,3,4,5,6,7,8,'Idle'])

#df.StatePfxRcd > 0
