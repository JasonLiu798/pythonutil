#!/usr/bin/env python
#-*- coding:utf-8 -*-

from threading import Timer
import time

import util.net.sshutil as shu
import util.file.csvutil as cu

INTERVAL=3


# res = shu.bssh(servers,'df -h',['x196',])
# if res:
    # print 'res type:',type(res)
    # for key in res.keys():
        # print 'key:',key,',output:',res.get(key)

servers=cu.parseSSH()


'''
def task():
    print 'task running'
    server = servers.get('x19')
    res = shu.sshNP(server['user'],server['ip'],server['port'],'~/.ssh/id_rsa.jianlong',execmd='date')
    print res
    # shu.bssh(servers,'df -h',['x196',])
'''
# t=Timer(INTERVAL,task)
# t.start()
server = servers.get('x19')
# startLine=getLine()



def getLine(filepath):
    # filepath='/data/logs/user/user.log.tmp'

    getLine="cat %s |wc -l" % filepath
    # cmd="cat /data/logs/user/user.log.tmp"
    cmdRet = shu.sshNP(server['user'],server['ip'],server['port'],'~/.ssh/id_rsa.jianlong',execmd=getLine)
    res = None
    if isinstance(cmdRet,list):
        if len(cmdRet)==1:
            res=cmdRet[0].replace("\n","")
    return res

def getContent(filepath,st,ed):
    # filepath='/dassh -p 22  -i ~/.ssh/id_rsa.jianlong work@192.168.143.19 'sed -n "5093,5125p" /data/logs/member-db-executor/member-db-executor.log.tmp'ta/logs/member-db-executor/member-db-executor.log.tmp'
    #filepath='/data/logs/user/user.log.tmp'
    setCmd='sed -n "%s,%sp" %s' % (st,ed,filepath)
    print setCmd
    # cutCmd='cut -d$"\\n" -f%s-%s %s' % (st,ed,filepath)
    # print cutCmd
    # cmd="cat /data/logs/user/user.log.tmp"
    cmdRet = shu.sshNP(server['user'],server['ip'],server['port'],'~/.ssh/id_rsa.jianlong',execmd=setCmd)
    # res = None
    return cmdRet

def main():
    first=True
    filepath='/data/logs/member-db-executor/member-db-executor.log.tmp'
    preLine = getLine(filepath)
    while True:
        time.sleep(INTERVAL)
        print 'main running'
        if first:
            first=False
        nowLine = getLine(filepath)
        print 'log line is %s' %  nowLine
        if preLine==nowLine:
            print 'same line'
            continue
        res=getContent(filepath,preLine,nowLine)
        preLine = nowLine

        # cmd="cat /data/logs/user/user.log.tmp"
        # res = shu.sshNP(server['user'],server['ip'],server['port'],'~/.ssh/id_rsa.jianlong',execmd=cmd)
        for i in res:
            print i,

# res=getContent(0,100)
# res = getLine()
# print res
#
main()



# res = shu.sshNP(server['user'],server['ip'],server['port'],'~/.ssh/id_rsa.jianlong',execmd='date')
# print res
