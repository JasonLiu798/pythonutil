#!/usr/bin/env python
#-*- coding:utf-8 -*-

# from util.net.sshutil import *
import util.net.sshutil as shu
import util.file.csvutil as cu

servers=cu.parseSSH()

res = shu.bssh(servers,'df -h',['x196',])
if res:
    # print 'res type:',type(res)
    for key in res.keys():
        print 'key:',key,',output:',res.get(key)

