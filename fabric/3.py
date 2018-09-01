#!/usr/bin/python2.6
#-*- coding: utf-8 -*-
from fabric.api import *
from fabric.colors import *
from fabric.context_managers import *
'''
这里为了简化工作，脚本采用纯python的写法，没有采用fabric的@task修饰器，脚本不需要利用fab执行，直接以python的形式执行即可
'''
user = 'ec2-user'
hosts=['bidder1','bidder2','bidder3','bidder4','bidder5','bidder6','bidder7','bidder8','bidder9','bidder10']
#机器数量比较多，这里只列出其中10台
@task
def put_task():
    print yellow("Put Local File to Nagios Client")
    with settings(warn_only=True):
        put("/home/ec2-user/check_cpu_utili.sh",
"/home/ec2-user/check_cpu_utili.sh")
        sudo("cp /home/ec2-user/check_cpu_utili.sh /usr/local/nagios/libexec")
        sudo("chown nagios:nagios /usr/local/nagios/libexec/check_cpu_utili.sh")
        sudo("chmod +x /usr/local/nagios/libexec/check_cpu_utili")
        sudo("kill  `ps aux | grep nrpe | head -n1 | awk '{print $2}' `")
        sudo("/usr/local/nagios/bin/nrpe -c /usr/local/nagios/etc/nrpe.cfg -d")
        print green("upload File success and restart nagios  service!")
        #这里以绿色字体打印结果是为了方便查看脚本执行结果

for host in hosts:
    env.host_string = host
    put_task()