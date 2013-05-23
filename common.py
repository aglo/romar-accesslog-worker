# -*- coding:utf-8 -*-
'''
Created on May 22, 2013

@author: outman
'''
import config
import pycurl
import sys
import urllib

class ParameterFormat:
    charset = None
    url = ''
          
    def __init__(self, charset):
        self.charset = charset
          
    def put(self,key,value):
        self.url = self.url + str(key) + '=' + urllib.quote(str(value).decode(sys.stdin.encoding).encode(self.charset)) + "&"
        
    def get_parameters_format(self):
        return self.url[0:len(self.url)-1]
    
def send_data_print(date, count):
    print date + ' ' + str(count)

#curl -d "tid=3553&dt=2012-10-24 18:12&data=100" http://10.10.3.43:9075/api/add-data 

def send_data(url_date, count):
#    paramter_format = format_parameter(url_date, count, config.tid)
    pf=ParameterFormat(config.encoding_charset)
    pf.put("tid", config.tid)
    pf.put("data", count)
    pf.put("dt", url_date) 
    c = pycurl.Curl()
    c.setopt(pycurl.URL, config.url + "?" + pf.get_parameters_format())
     
    # 最大重定向次数,可以预防重定向陷阱    
    c.setopt(pycurl.MAXREDIRS, 5)
      
    # 连接超时设置    
    c.setopt(pycurl.CONNECTTIMEOUT, 60)
    c.setopt(pycurl.TIMEOUT, 300)
      
    #访问,阻塞到访问结束
    c.perform() 
    
def get_date_from_line(line):
    pos = line.find("/", 16, 26)
    date = line[pos - 2:pos + 14]
    return date
 
def get_status_from_line(line):
    rpos = line.rfind('"');
    length = len(line)
    end = line[rpos + 2:length - 1]
    status = end.split(' ')[0]
    return status   