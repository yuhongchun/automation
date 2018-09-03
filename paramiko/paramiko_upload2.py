#paramiko for upload(2)
# -*- coding: utf-8 -*-
#!/usr/bin/python
import paramiko
#输入需要连接的ip地址
t = paramiko.Transport(("IP",22))
#用户密码
t.connect(username = "用户名", password = "口令")
#调用SFTPClient类的from_transport方法
sftp = paramiko.SFTPClient.from_transport(t)
#需要上传的远程服务器路径
remotepath='/root/a.tar.gz'
#本地文件路径
localpath='/root/a.tar.gz'
sftp.put(localpath,remotepath)
#关闭连接
t.close()



