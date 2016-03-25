#!/usr/bin/env python
#-*- coding:utf-8 -*-

import platform
import util.common.stringutil as su

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

