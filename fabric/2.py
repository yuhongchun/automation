#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from fabric.api  import *
from fabric.colors import *
env.disable_known_hosts=True
env.timeout=20
env.user = 'root'
env.hosts = ['193.112.1.2','193.112.1.3','111.230.1.4','111.231.1.5','111.230.1.6','134.175.1.7','193.112.1.8','193.112.1.2','111.230.1.3','134.175.1.4','193.112.1.5']
env.password = 'password'
# 此处输入共用密码

@task
def work():
    run("docker login -u=daoclounuser -p=daocloundpasswd ccr.ccs.tencentyun.com")
    print yellow("此机器自动登陆成功！")
'''
注意 fabric的版本，高版本的fabirc去掉了fabric.api，这里推荐用pip安装，命令如下所示：
pip install fabric==1.14.0
'''