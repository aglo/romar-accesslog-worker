# -*- coding:utf-8-*-

'''
Created on May 17, 2013

@author: outman
'''

import time
import random
import config

ip = '"GET /items/similars?item=00000246580338385&limit=10 HTTP/1.1"'

time_sleep = (0.1, 0.2, 1, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.05)
length = len(time_sleep) - 1

filePath = config.filepath

while True:
    index = random.randint(1, length)
    time.sleep(time_sleep[index])
    log_line = str(random.randint(1, 255)) + "." + str(random.randint(1, 255)) + "."
    log_line = log_line + str(random.randint(1, 255))+"." + str(random.randint(1, 255))
    log_line = log_line + " - - - "
    date_now = time.localtime(time.time())
    date_string = time.strftime("%d/%m/%Y:%H:%M:%S", date_now)
    log_line = log_line + date_string + " +0800 "
    log_line = log_line + ip + " 200 " + str(random.randint(1, 1000)) + "\n"
    f = open(filePath, "a")
    f.write(log_line)
    f.close()