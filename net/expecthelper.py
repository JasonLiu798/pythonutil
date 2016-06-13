#!/bin/env python
#-*- coding:utf-8 -*-

import os,sys
# import pexpect
# from pexpect import *

def ssh_cmd(ip, user, passwd, cmd):
    # ssh = pexpect.spawn('ssh %s@%s "%s"' % (user, ip, cmd))
    # r=ssh.read()
    # print 'first',r
    '''
    try:
        i = ssh.expect(['password: ', 'continue connecting (yes/no)?'])
        print 'expect res ',i
        if i == 0 :
            ssh.sendline(passwd)
            r = ssh.read()
        elif i == 1:
            ssh.sendline('yes\n')
            ssh.expect('password: ')
            ssh.sendline(passwd)
            r = ssh.read()
    except pexpect.EOF:
        print 'exception'
        r = ssh.read()
        ssh.close()
    '''
    # ssh.close()
    # return r




#name ip port user pass
# for host in hosts.split("\n"):
#     if host:
#         name, ip, port, user, passwd = host.split(" ")
#         cmds='df -h,uptime'
#         for cmd in cmds.split(","):
#             print "-- %s run:%s --" % (ip, cmd)
#             print ssh_cmd(ip, user, passwd, cmd)
