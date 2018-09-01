#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
import logging
from fabric.api import *
from fabric.colors import *

env.timeout = 20
env.port = '12321'
env.key_filename = "/root/.ssh/id_dsa"
env.disable_known_hosts = True


# 操作此项时注意安全问题，谨慎操作
def local_task(platform):
    with settings(hide('running', 'stdout'), warn_only=True):
        cmd_output = local("/work/ulitytools/get_platform_hosts -p %s >%s" % (platform, platform))
```
/ work / ulitytools / get_platform_hosts是我们自行研发的程序，可以从公司的CMDB系统动态获取平台对应主机的IP地址
```
if cmd_output.return_code == 0:
    l = []
    with open(platform) as f:
        for line in f:
            l.append(line.strip())
    return l


def do_task():
    logging.basicConfig(level=logging.ERROR)


```
如果我们把level设成
logging.ERROR的时候，所有debug() | info() | warning()
的讯息将被忽略
```
platform_list = {}
for p in ["c01.i01", "c01.i02", "c01.i03", "c01.i04", "c01.i05", "c02.i01", "c02.i02", "c02.p03", "c02.i04", "c03.i03"]:
    ret = execute(Local_task, p)
    platform_list[p] = ret['<local-only>']
env.roledefs = platform_list

do_task()
```
注意，env.roledefs为全局变量，如果放在do_task1函数里面执行，会导致roles报错，现象为提示c01.i77等角色不存在
这里我们可以根据角色名来分配不同的函数，执行相应的任务, 例如下面的do_task1和do_task函数对应的操作，fabric角色的灵活性在这里体现得淋漓尽致
```


@roles("c01.i01", "c01.i02", "c01.i03")
def do_task1():
    run('hostname')


@roles("c02.i02", "c02.i04")
def do_task2():
    run('df -h')

#/work/ulitytools/get_platform_hosts是我们用perl自行研发的程序，可以从公司的CMDB系统动态获取平台对应主机的平台信息、线路信息及IP地址等（如果是三线机器，以电信IP为主）