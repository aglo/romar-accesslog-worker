# -*- coding:utf-8 -*-

'''
Created on May 15, 2013

@author: outman
'''
import config
import sys
import time
import pycurl

filePath = config.filepath

def get_lines_from_file():
    try:
        f = open(filePath, 'r')
        lines = f.readlines()
        f.close()
        return lines
    except IOError:
            print "the file no found"
            sys.exit()
        
def get_minute_from_line(line):
    pos = line.find("/", 16, 26)
    minute = line[pos + 12:pos + 14]
    return minute

def get_date_from_line(line):
    pos = line.find("/", 16, 26)
    date = line[pos - 2:pos + 14]
    return date
 
def get_status_from_line(line):
    rpos = line.rfind('"');
    length = len(line)
    end = line[rpos + 2:length - 1]
    status = end.split(" ")[0]
    return status

def cmp_string(str1, str2):
    return cmp(str1, str2)

def string_logdate_to_datetime(s): 
    return time.strptime(s, config.log_date_format)
    
def get_count_time(time_desc):
    f = open(filePath, 'r')
    lines = f.readlines()
    f.close()
    flag = 0
    count = 0
    for line in lines:
        
        log_date = string_logdate_to_datetime(get_date_from_line(line))
        status = get_status_from_line(line)
        
        if log_date == time_desc and cmp_string(status,"200") == 0:
            count = count + 1
            flag = 1
        
        if flag == 1 and log_date != time_desc:
            break    
    return count   
        
def get_count_between_time(begin_time, end_time):
    f = open(filePath, 'r')
    lines = f.readlines()
    f.close()
    count = 0
    date_now=begin_time
    for line in lines:
        if line == '\n':
            continue
        
        log_date = string_logdate_to_datetime(get_date_from_line(line))
        status = get_status_from_line(line)
        
        if begin_time <= log_date and log_date <= end_time:
            
            if date_now == log_date and cmp(status, "200")==0:
                count = count + 1
                
            else:
                url_date=time.strftime(config.url_date_format, date_now)
                send_data(url_date, count)
                count = 1
                date_now = log_date
                
        elif log_date > end_time:
                url_date=time.strftime(config.url_date_format, date_now)
                send_data(url_date, count)
                break                         

# curl -d "tid=3553&dt=2012-10-24 18:12&data=100" http://10.10.3.43:9075/api/add-data 

def format_parameter(url_date, data, tid):
    string_desc = "tid=" +str(tid) + "&"
    string_desc = string_desc + "dt=" + url_date +"&"
    string_desc = string_desc + "data=" +data
    return string_desc

# def send_data(date, count):
#     print date
#     print count

def send_data(url_date, count):
    paramter_format=format_parameter(url_date, count, config.tid)
    c = pycurl.Curl()
    c.setopt(pycurl.URL, config.url + "?" + paramter_format)
     
    # 最大重定向次数,可以预防重定向陷阱    
    c.setopt(pycurl.MAXREDIRS, 5)
      
    # 连接超时设置    
    c.setopt(pycurl.CONNECTTIMEOUT, 60)
    c.setopt(pycurl.TIMEOUT, 300)
      
    #访问,阻塞到访问结束
    c.perform()  
        
if __name__ == '__main__':
    
    if len(sys.argv) < 2 or len(sys.argv)>3:
        print "No action specified."
        sys.exit()
        
    if len(sys.argv) == 2:
        date_desc = sys.argv[1]
        
        try:
            d = time.strptime(date_desc, config.config_date_format)
            print get_count_time(d)
            
        except:
            print "the time is error"    
            
    if len(sys.argv) == 3:      
        try:
            string_begin_time = sys.argv[1]          
            string_end_time = sys.argv[2]
                    
            begin_time = time.strptime(string_begin_time, config.config_date_format)       
            end_time = time.strptime(string_end_time, config.config_date_format)
            
            if begin_time > end_time:
                print "the begin time after the end time"
                
            else:                
                get_count_between_time(begin_time, end_time)           
        except:           
            print "the time is error"
