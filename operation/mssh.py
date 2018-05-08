# -*- coding: utf-8 -*-
#edit by yoyo20180508
from multiprocessing import Process,Pool
import paramiko
import sys,os

host_list =(
	('127.0.0.1','root','yoyo19810204'),
        ('127.0.0.1','root','yoyo19810204')
)

s = paramiko.SSHClient() #绑定实例
s.load_system_host_keys()  #加载本机host文件
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def ssh_run(host_info,cmd):
	ip,username,password = host_info
	s.connect(ip,22,username,password,timeout=5) #连接远程主机
        stdin,stdout,stderr = s.exec_command(cmd)  #执行命令
        cmd_result = stdout.read(),stderr.read()   #读取命令结果
	print '\033[32;1m---------------%s----------------------\033[0m' % ip,username
        for line in cmd_result:
        	print line,

p = Pool(processes=2)
result_list =[]

for h in host_list:
	result_list.append(p.apply_async(ssh_run,[h,'uptime']))

for res in result_list:
	print res.get()
s.close
