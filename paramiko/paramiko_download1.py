#paramiko for download
# -*- coding: utf-8 -*-
#!/usr/bin/python
import paramiko
#输入需要连接的ip地址
t = paramiko.Transport(("IP",22))
#用户密码
t.connect(username = "用户名", password = "口令")
#调用SFTPClient类的from_transport方法
sftp = paramiko.SFTPClient.from_transport(t)
remotepath='/tmp/test.txt'
localpath='/tmp/test.txt'
sftp.get(remotepath, localpath)
#关闭连接
t.close()



