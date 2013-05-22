# -*- coding:utf-8 -*-

'''
Created on May 15, 2013

@author: outman
'''
import config
import sys
import time
import common

def get_lines_from_file():
    try:
        f = open(config.configpath, 'r')
        lines = f.readlines()
        f.close()
        return lines
    except IOError:
            print "the file no found"
            sys.exit()        

def string_logdate_to_datetime(s): 
    return time.strptime(s, config.log_date_format)

def datetime_format_to_urldate(date_desc):
    return time.strftime(config.url_date_format, date_desc)

def configdate_format_to_datetime(date_desc):
    return time.strptime(date_desc, config.config_date_format)
    
def get_count_time(time_desc):
    f = open(config.filepath, 'r')
    lines = f.readlines()
    f.close()
    flag = 0
    count = 0
    
    for line in lines:
        
        log_date = string_logdate_to_datetime(common.get_date_from_line(line))
        status = common.get_status_from_line(line)
        
        if log_date == time_desc and status == '200':
            count = count + 1
            flag = 1
        
        if flag == 1 and log_date != time_desc:
            break
           
    url_date = time.strftime(config.url_date_format, time_desc) 
    common.send_data_print(url_date,count)
#    common.send_data(url_date,count)   
        
def get_count_between_time(begin_time, end_time):
    f = open(config.filepath, 'r')
    lines = f.readlines()
    f.close()
    count = 0
    log_date = None
    date_now = begin_time
    for line in lines:
        if line == '\n' or len(line) == 0:
            continue
        
        log_date = string_logdate_to_datetime(common.get_date_from_line(line))
        status =common.get_status_from_line(line)
        
        if begin_time <= log_date and log_date <= end_time:
            
            if date_now == log_date and status == '200':
                count = count + 1
                
            else:
                url_date = datetime_format_to_urldate(log_date)
                common.send_data_print(url_date, count)
#                common.send_data(url_date, count)                
                count = 1
                date_now = log_date
                
        elif log_date > end_time:
                url_date = datetime_format_to_urldate(date_now)
                common.send_data_print(url_date, count)
#                common.send_data(url_date, count)
                break 
    if log_date <= end_time:
        url_date = datetime_format_to_urldate(log_date)
        common.send_data_print(url_date, count)
#         common.send_data(url_date,count)                    

# curl -d "tid=3553&dt=2012-10-24 18:12&data=100" http://10.10.3.43:9075/api/add-data 

def get_datenow():
    date_string = time.strftime(config.url_date_format, time.localtime(time.time()))
    return time.strptime(date_string, config.url_date_format)  

        
if __name__ == '__main__':
    
    datenow = get_datenow()
    
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print "No action specified!!"
        sys.exit(0)
        
    if len(sys.argv) == 2:
        try:
            date_desc = sys.argv[1]
            if len(date_desc) != 12:
                sys.exit(0)  # 此方法是正常退出，会抛出一个SystemExit异常                
            d = configdate_format_to_datetime(date_desc)
            if d >= datenow:
                print "the time must before now!!"
            else:
                get_count_time(d)
        except:
            print "the time is error!!"    
            
    if len(sys.argv) == 3:      
        try:
            string_begin_time = sys.argv[1]          
            string_end_time = sys.argv[2]
            
            if len(string_begin_time) != 12 or len(string_end_time) != 12:
                sys.exit(0)  # 此方法是正常退出，会抛出一个SystemExit异常 
                        
            begin_time = time.strptime(string_begin_time, config.config_date_format)       
            end_time = time.strptime(string_end_time, config.config_date_format)
            
            if begin_time > end_time:
                print "the begin time after the end time!!"
                
            elif begin_time >= datenow:
                print "the begin time must before now!!"
                 
            elif end_time >= datenow:
                print "the end time must before now!!"     
            else:                
                get_count_between_time(begin_time, end_time)
                           
        except:           
            print "the time is error!!"
