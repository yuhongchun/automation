#paramiko for upload(1)
#!/usr/bin/env python
#encoding:utf8
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh 连接的用户密码
ssh.connect("ip",22,"root", "密码")
#需要执行的命令
stdin, stdout, stderr = ssh.exec_command("ls")
print stdout.readlines()
#关闭连接
ssh.close()


