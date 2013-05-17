'''
Created on May 16, 2013

@author: outman
'''
import time
import random

ip = '"GET /items/similars?item=00000246580338385&limit=10 HTTP/1.1"'
time_sleep = (0.1,0.2,1,0.4,0.5,0.6,0.7,0.8,0.9,0.05)
length = len(time_sleep)-1
filePath = "test.log"
while True:
    index = random.randint(1,length)
    time.sleep(time_sleep[index])
    f = open(filePath,"a")
    f.write(str(random.randint(1, 255)))
    f.write(".")
    f.write(str(random.randint(1, 255)))
    f.write(".")
    f.write(str(random.randint(1, 255)))
    f.write(".")
    f.write(str(random.randint(1, 255)))
    f.write(" - - - ")
    date_now = time.localtime(time.time())
    date_string = time.strftime("%d/%m/%Y:%H:%M:%S",date_now)
    f.write(date_string)
    f.write(" +0800 ")
    f.write(ip)
    f.write(' 200 ')
    f.write(str(random.randint(1, 1000)))
    f.write("\n")
    f.close()