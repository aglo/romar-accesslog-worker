romar-accesslog-worker
======================

定时分析romar进程产生的accesslog
## 功能需求
* 对于给定日志定时抓取并且进行分析和统计
* 把统计的结果发送给其他应用

## Usage

##### 参数配置

* 安装pycurl模块
* 在config.py修改configpath路径，此路径为日志相对与此文件的相对路径

```python
python monitord.py
```

* 输出

从启动时间的下一分钟开始统计
输出时间和统计结果 输出结果格式 "%Y%m%d %H:%M 统计结果"，例："2013-05-20 14:27 61"  

```python
python monitor.py  time  |  python monitor.py starttime  endtime
```

* 运行

运行'python monitorD.py time' 输出这分钟的统计值 
运行'python monitorD.py starttime endtime' 输出这段时间间隔的内的每一分钟统计结果
统计结果包括starttime和endtime这两个时间段，如果某分钟没数据则不输出
**时间格式**："%Y%m%d%H%m"  例如要输入时间为："2013-05-20 14:27"，输入'201305201427'即可 

* 输出

直接在命令行输出时间和统计结果 输出结果格式 “%Y%m%d %H:%M 统计结果”，例："2013-05-20 14:27  61" 