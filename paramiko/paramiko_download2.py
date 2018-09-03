#!/usr/bin/env python
#encoding:utf8
import paramiko
# 创建ssh对象
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
with open("targe", 'r') as fp:
    for line in fp:
        ip = line.strip()
        ssh.connect(ip, 22, "root", 密码)
        stdin, stdout, stderr = ssh.exec_command("sh /root/test.sh")
        str = stdout.readlines()

ssh.close()



