import time 
from datetime import datetime as dt

path=r"C:/windows/system32/drivers/etc/hosts"

direct="127.0.0.1"
l=[]
n=int(input("Enter the number of websites to be blocked"))
print("Enter the url of the website")
for i in range(n):
     x=input()
     l.append(x)     
     


if dt(dt.now().year,dt.now().month,dt.now().day,8) <dt.now()< dt(dt.now().year,dt.now().month,dt.now().day,16):
     print("Website blocked...")
     with open(path,'r+') as file:
            content=file.read()
            for j in l:
                if j in content:
                    pass
                else:
                    file.write("\t"+direct+"\t"+j+"\n")
else:
    with open(path,'r+') as file:
        content=file.readlines()
        file.seek(0)
        for line in content:
            if not any(j in line for j in l):
                file.write(line)

                    
        file.truncate()
        print("Website unblocked..")
