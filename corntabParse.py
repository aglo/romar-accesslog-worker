'''
Created on May 15, 2013

@author: outman
'''


import time


filePath = "example/example.log"

def get_lines_from_file():
    try:
        f =open(filePath, 'r')
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
    
def get_count_time(date_desc):
    f = open(filePath, 'r')
    lines = f.readlines()
    f.close()
    flag = 0
    count = 0
    length = len(lines)
    length = length-1
    while length >= 0:
        length = length-1
        log_date = string_logdate_toDatetime( get_date_from_line( lines[length] ) )
       
        status = get_status_from_line(lines[length])
        
        if log_date == date_desc and cmp_string(status,"200") == 0:
            count = count+1
            flag = 1
        
        if flag == 1 and log_date != date_desc:
            break    
    return count   
        
 
if __name__ == '__main__':
    
    date_now = time.localtime(time.time()-60)
    date_string = time.strftime("%Y%m%d%H%M",date_now)
    date_desc = time.strptime(date_string,"%Y%m%d%H%M")
    print get_count_time(date_desc)