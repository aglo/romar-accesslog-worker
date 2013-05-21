# -*- coding:utf-8 -*-

'''
Created on May 15, 2013

@author: outman
'''

import sys
import config
import time
import pycurl

filePath = config.filepath

fpos = 0

def get_lines_from_file():
    
    global fpos
    try:
        f = open(filePath, 'r')
        f.seek(fpos)
        lines = f.readlines()
        fpos = f.tell()
        f.close()
        return lines
    except IOError:
            print "the file no found"
            sys.exit()
        
def get_minute_from_line(line):
    pos = line.find('/', 16, 26)
    minute = line[pos + 12:pos + 14]
    return minute

def get_date_from_line(line):
    pos = line.find("/", 16, 26)
    date_string = line[pos - 2:pos + 14]
    return date_string
 
def get_status_from_line(line):
    rpos = line.rfind('"');
    length = len(line)
    end = line[rpos + 2:length - 1]
    status = end.split(' ')[0]
    return status

def cmp_string(str1, str2):
    return cmp(str1, str2)

def string_logdate_to_urldate(log_time):
    log_time_tmp=time.strptime(log_time, config.log_date_format)
    return time.strftime(config.url_date_format, log_time_tmp)

# curl -d "tid=3553&dt=2012-10-24 18:12&data=100" http://10.10.3.43:9075/api/add-data 

def format_parameter(url_date, data, tid):
    string_desc = 'tid=' + str(tid) + '&'
    string_desc = string_desc + 'dt=' + url_date + '&'
    string_desc = string_desc + 'data=' +data
    return string_desc

def send_data_print(log_date, count):
    urldate = string_logdate_to_urldate(log_date)
    print urldate+" "+str(count)
  
def send_data(log_date, count):
    urldate = string_logdate_to_urldate(log_date)
    paramter_format=format_parameter(urldate, count, config.tid)
    c = pycurl.Curl()
    c.setopt(pycurl.URL, config.url + "?" + paramter_format)
    
    # 最大重定向次数,可以预防重定向陷阱    
    c.setopt(pycurl.MAXREDIRS, 5)
     
    # 连接超时设置   
    c.setopt(pycurl.CONNECTTIMEOUT, 60)
    c.setopt(pycurl.TIMEOUT, 300)
     
    #访问     
    c.perform()

    
if __name__ == '__main__':
    count = 0
    minuteNow = ""
    minute = ""
    fpos = 0
    log_date = ""

    while True:
        lines = get_lines_from_file()
        
        while len(lines) == 0:
            lines = get_lines_from_file()
            
        for line in lines: 
            if line == '\n':
                continue   
            minute = get_minute_from_line(line)
            status = get_status_from_line(line)
            
            if len(minuteNow) == 0 or cmp("", minuteNow) == 0:
                minuteNow = get_minute_from_line(line)
                log_date = get_date_from_line(line)
                
            if cmp_string(minuteNow, minute) == 0 and cmp_string(status,"200") == 0:
                count = count + 1
                
            if cmp(minuteNow,minute) != 0:
#                send_data(log_date, count)
                send_data_print(log_date,count)
                log_date = get_date_from_line(line)
                minuteNow = minute
                count = 1
