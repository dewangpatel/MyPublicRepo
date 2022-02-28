import os
import netmiko
import datetime
import re
import pandas as pd

os.chdir('C:\\temp')
os.getcwd()

## commands needs to be send to cisco device and output to bgp.txt file


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

for d in range (len(df.StatePfxRcd.isin([0,1,2,3,4,5,6,7,8,'Idle']))):
	print(df.StatePfxRcd.isin([0,2,3,4,5,6,7,8,'Idle'])[d])

#df.StatePfxRcd > 0


#==========
#STEP 2
## commands needs to be send to cisco device and output to mroutex.txt file

address = input("Enter IP Address: ")

match = re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", address)
print(bool(match))
if (bool(match)) == True:
    print('')

with open('mroute.txt', "r") as textfile1:
    textlines1 = textfile1.read().splitlines()
    
bb=0
for aa in range(len(textlines1)):
    if ("Active Flow" in textlines1[bb]):
        print("Active Flow Found")
        print(bb)
        cc=bb+1
        #textfile.write(textlines[b]+"\n")
    bb+=1
bb=0
for aa in range(len(textlines1)):
    if ("Inactive Flow" in textlines1[bb]):
        print("Inactive Flow Found")
        print(bb)
        cc=bb+1
        #textfile.write(textlines[b]+"\n")
    bb+=1


# =============================
# STEP 3
## commands needs to be send to cisco device and output to mroutex.txt file

with open('mroute1.txt', "r") as textfile2:
    textlines2 = textfile2.read().splitlines()
bbb=0
for aaa in range(len(textlines2)):
    if ("SR:" in textlines2[bbb]):
        print("SR: Line Found")
        print(textlines2[bbb])
        #myline=(textlines2[bbb])
        #myline.split()[2][:-1]
        grabedip = (textlines2[bbb]).split()[2][:-1]
        print((textlines2[bbb]).split()[2][:-1])
        print(grabedip)
        ccc=bbb+1
        #textfile.write(textlines[b]+"\n")
    bbb+=1


# =============================
# STEP 4

## commands needs to be send to cisco device and output to mroutex.txt file

with open('mroute2.txt', "r") as textfile3:
    textlines3 = textfile3.read().splitlines()
    
bbbb=0
for aaaa in range(len(textlines3)):
    if ("Active Flow" in textlines3[bbbb]):
        print("Active Flow Found")
        print(bbbb)
        cccc=bbbb+1
    bbbb+=1

bbbb=0
for aaaa in range(len(textlines3)):
    if ("InActive" in textlines3[bbbb]):
        print("InActive Flow Found")
        print(bbbb)
        cccc=bbbb+1
    bbbb+=1
