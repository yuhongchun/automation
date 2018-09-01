#!/usr/bin/python
# -*- coding: utf-8 -*-
from fabric.api import *
from fabric.colors import *
from fabric.context_managers import *

env.user = 'root'
env.hosts = ['192.168.1.200','192.168.1.205','192.168.1.206']
env.password = 'redhat'

@task
def git_update():
    with settings(warn_only=True):
        with cd('/home/project/github'):
            sudo('git stash clear')
            #清理当前git中所有的储藏，以便于我们stashing最新的工作代码
            sudo('git stash')
            '''
            如果我们想切换分支，但是又不想提交正在进行中的工作,所以得储藏这些变更。为了往git堆栈推送一个新的储藏，只需要运行git stash命令即可
            '''
            sudo('git pull')
            sudo('git stash apply')
            #完成当前代码pull以后，取回最新的stashing工作代码，这里我们用命令git stash apply
            sudo('nginx -s reload')
'''
for host in env.hosts:
    env.host_string = host
    git_update()
'''
