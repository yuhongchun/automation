#!/usr/bin/env python
#encoding:utf8
import paramiko
class Cmd_ssh(object):
    key=None
    def __init__(self,host,user='admin',password='admidsa@qss',pkey=None):
        self.user=user
        self.password=password
        self.host=host
        self.pkey=pkey
        self.ssh=paramiko.SSHClient()

    def _close(self):
        return self.ssh.close()
    def _key_ssh(self,cmd):
        try:
            self.ssh = paramiko.SSHClient()
            self.key=paramiko.RSAKey.from_private_key_file(self.pkey)
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(self.host,username = self.user,pkey=self.key)
            stdin,stdout,stderr=self.ssh.exec_command(cmd)
            channel = stdout.channel
            status = channel.recv_exit_status()
            if status==0:
                result = get_result(0, stdout.read().strip())
            else:
                result = get_result(1,stderr.read().strip())
            self.ssh.close()
            return result
        except Exception,e:
            return get_result(1,str(e))


    def _upload(self,local_file,remote_file):
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.load_system_host_keys()
            self.ssh.connect(self.host,username = self.user,pkey=self.key)
            sftp = paramiko.SFTPClient.from_transport(self.ssh.get_transport())
            sftp = self.ssh.open_sftp()
            sftp.put(local_file, remote_file)
            self.ssh.close()
            return get_result(0,'done')
        except Exception,e:
            return get_result(1,str(e))
    def run(self,cmd='id'):
        # if self.key:
        return self._key_ssh(cmd)
        # else:
        #     return self._passwd_ssh(cmd)
    def upload(self,local_file,remote_file):
        return self._upload(local_file,remote_file)
