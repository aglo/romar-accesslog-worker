'''
Created on May 15, 2013

@author: outman
'''

import sys
import time
# import traceback

filePath = "example/example.log"
def get_lines_from_file():
    try:
        f = open(filePath, 'r')
        lines = f.readlines()
        f.close()
        return lines
    except IOError:
            pass
        
def get_minute_from_line(line):
    pos = line.find("/",16,26)
    minute = line[pos+12:pos+14]
    return minute

def get_date_from_line(line):
    pos = line.find("/",16,26)
    date = line[pos-2:pos+14]
    return date
 
def get_status_from_line(line):
    rpos = line.rfind('"');
    length = len(line)
    end = line[rpos+2:length-1]
    status = end.split(" ")[0]
    return status

def cmp_string(str1,str2):
    return cmp(str1,str2)

def send_data(date,count):
    print date
    print count

def string_logdate_toDatetime(s): 
    return time.strptime(s, "%d/%m/%Y:%H:%M")
    
def get_count_time(time_desc):
    f = open(filePath, 'r')
    lines = f.readlines()
    f.close()
    flag = 0
    count = 0
    for line in lines:
        
        log_date = string_logdate_toDatetime( get_date_from_line( line ) )
       
        status = get_status_from_line(line)
        
        if log_date == time_desc and cmp_string(status,"200")==0:
            count = count+1
            flag = 1
        
        if flag == 1 and log_date != time_desc:
            break    
    return count   
        
def get_count_between_time(begin_time, end_time):
    f = open(filePath, 'r')
    lines = f.readlines()
    f.close()
    flag = 0
    count = 0
    for line in lines:
        log_date = string_logdate_toDatetime( get_date_from_line( line ) )
        status = get_status_from_line(line)
        if begin_time <= log_date and log_date <= end_time and cmp_string(status,"200") == 0:
            count = count+1
            flag = 1
        if flag == 1 and (begin_time > log_date or log_date > end_time):
            break
    return count   
        
if __name__ == '__main__':
    if len(sys.argv) < 2 or len(sys.argv)>3:
        print 'No action specified.'
        sys.exit()
        
    if len(sys.argv) == 2:
        date_desc = sys.argv[1]
        
        try:
            d = time.strptime(date_desc,"%Y%m%d%H%M")
            print get_count_time(d)
        except:
#            traceback.print_exc(file=sys.stdout)
            print "the time is error"    
            
    if len(sys.argv) == 3:
        
        try:
            string_begin_time = sys.argv[1]
            
            string_end_time = sys.argv[2]
         
            begin_time = time.strptime(string_begin_time,"%Y%m%d%H%M")
       
            end_time = time.strptime(string_end_time,"%Y%m%d%H%M")
            
            print get_count_between_time(begin_time,end_time);
        except:
#            traceback.print_exc(file=sys.stdout)
            print "the time is error"
