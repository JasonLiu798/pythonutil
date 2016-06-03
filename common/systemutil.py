#!/usr/bin/env python
#-*- coding:utf-8 -*-

import platform
import util.common.stringutil as su
import subprocess

import util.log.logutil as logutil
log = logutil.LogUtil.getStdLog()

#log = logger.Logger(loglevel=1, logger="stdout").getlog()


WINDOWS='WIN'
LINUX='LINUX'
CYGWIN='CYGWIN'
MAC='DARWIN'

def getOS():
    osname = platform.system().upper()
    # print osname
    if su.startWith(osname,WINDOWS):
        return WINDOWS
    elif su.startWith(osname,LINUX):
        return LINUX
    elif su.startWith(osname,CYGWIN):
        return CYGWIN
    elif su.startWith(osname,MAC):
        return MAC

def shellExec(cmd,debugLog=True):
    # log.info('exec: '+cmd)
    # print 'exec',cmd
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    lines = p.stdout.readlines()
    # print 'type ',type(lines),'lines',lines
    # for line in p.stdout.readlines():
        # print line
    retval = p.wait()
    log.info('ret:'+str(retval))
    if debugLog:
        log.debug('res:'+str(lines))
    # for l in lines:
    #     log.info(l)
    if retval!=0:
        log.error('ssh exec %s fail' % cmd)
        return False,None
    else:
        return True,lines


'''
command:find
'''
def find(directory,name,ftype='f'):
    if directory:
        cmd='find '+directory+' '
    else:
        raise Exception,'directory is null'
    if name:
        cmd+='-name '+name+' '
    else:
        raise Exception,'name is null'
    cmd+='-type '+ftype
    status,ret=shellExec(cmd)
    if status:
        ret=su.removeLineSep(ret)
        return ret
    else:
        return None

# print find('/opt/projectL','target','d')


# print getOS()


'''
import time, threading

def loop():
    print 'thread %s is running...' % threading.current_thread().name
    n = 0
    while n < 5:
        n = n + 1
        print 'thread %s >>> %s' % (threading.current_thread().name, n)
        time.sleep(1)
    print 'thread %s ended.' % threading.current_thread().name

print 'thread %s is running...' % threading.current_thread().name
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print 'thread %s ended.' % threading.current_thread().name
'''

