#!/bin/env python
#-*- coding:utf-8 -*-

import os,sys
import pexpect
# from pexpect import *

def ssh_cmd(ip, user, passwd, cmd):
    ssh = pexpect.spawn('ssh %s@%s "%s"' % (user, ip, cmd))
    r=ssh.read()
    print 'first',r
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
    ssh.close()
    return r

hosts = '''
dp113 192.168.143.79 22 guest guest
'''
#dm118 192.168.143.118 22 work work
#192.168.1.12:root:1357924680:df -h,uptime
for host in hosts.split("\n"):
    if host:
        name, ip, port, user, passwd = host.split(" ")
        cmds='df -h,uptime'
        for cmd in cmds.split(","):
            print "-- %s run:%s --" % (ip, cmd)
            print ssh_cmd(ip, user, passwd, cmd)
