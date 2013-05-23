romar-accesslog-worker
======================

定时分析romar进程产生的accesslog

## 功能需求
* 对于给定日志定时抓取并且进行分析和统计
* 把统计的结果发送给其他应用

## Usage

1. 修改`config.py`中的`configpath`变量，此路径为日志文件路径
2. 如果在测试环境，我们准备了一个测试脚本来生成模拟数据

```
$ python -m test/fake
```

### monitord

```
python monitord.py
```

无需参数启动，从下一分钟开始统计。

生产环境中我们将作为守护进程启动

```
nohup python monitord.py &
```

输出时间和统计结果 输出结果格式 "%Y%m%d %H:%M {$num}"，例："2013-05-20 14:27 61"  

### monitor

与monitord不同，此脚本用来统计指定时间或时间段内的访问数量，所以至少将需要一个参数。

```
python monitor.py  time 
```

time的格式指定为`%Y%m%d%H%m`，例："201305201427"。将输出指定的该分钟访问次数。

```
python monitor.py  starttime endtime 
```
starttime与endtime格式相同。将输出指定时间段内每分钟的访问次数。

以上的结果输出格式均与monitord相同。

