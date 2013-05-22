# -*- coding:utf-8 -*-

'''
Created on May 15, 2013

@author: outman
'''

import sys
import config
import time
import os
import common

fpos = os.stat(config.filepath)[6]

def get_lines_from_file():
    
    global fpos
    try:
        f = open(config.filepath, 'r')
        f.seek(fpos)
        lines = f.readlines()
        fpos = f.tell()
        return lines
    except IOError:
            print "the file no found"
            sys.exit()

def string_logdate_to_urldate(log_date):
    log_date_tmp = time.strptime(log_date, config.log_date_format)
    return time.strftime(config.url_date_format, log_date_tmp)

def get_now_urldate_string():
    datenow = time.localtime(time.time() + 1*60)
    date_string = time.strftime(config.url_date_format, datenow)
    return date_string

if __name__ == '__main__':
    count = 0
    flag = 0
    minuteNow = get_now_urldate_string();

    log_date = None

    while True:
        lines = get_lines_from_file()
        
        while len(lines) == 0:
            time.sleep(3)   # 睡眠时间不确定，或者可以不睡眠
            lines = get_lines_from_file()
            
        for line in lines: 
            if line == '\n' or len(line) == 0:
                continue   
            
            log_date_tmp = common.get_date_from_line(line)
            log_date = string_logdate_to_urldate(log_date_tmp)
            
            if flag == 0:
                if minuteNow == log_date:
                    flag = 1
                    count = count + 1
                continue
                
            status = common.get_status_from_line(line)
                        
            if minuteNow == log_date and status == '200':
                count = count + 1
                
            if cmp(minuteNow,log_date) != 0:
#                 common.send_data(log_date, count)
                common.send_data_print(minuteNow, count)
                minuteNow = log_date
                log_date = common.get_date_from_line(line)
                count = 1