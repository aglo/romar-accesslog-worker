# -*- coding:utf-8 -*-
'''
Created on May 17, 2013

@author: outman
'''

import os

abspath = os.path.abspath(os.path.join(os.getcwd(),  __file__))
configpath = "./test/test.log"   # 此路径为日志相对与此文件的相对路径
filepath = abspath[0:abspath.rfind("/") + 1] + configpath

log_date_format = '%d/%m/%Y:%H:%M'  # 日志时间格式
url_date_format = '%Y-%m-%d %H:%M'  # 服务器接受的时间格式
config_date_format = '%Y%m%d%H%M'   # 命令行接收的时间格式

url = 'http://10.10.3.43:9075/api/add-data' 

tid=3553


