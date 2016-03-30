#!/bin/env python
#-*- coding:utf-8 -*-

import re

def startWith(str,startstr):
    res = True
    if len(startstr)<=0:
        return res
    if len(str)>0:
        for i in range(min(len(str),len(startstr))):
            if str[i]!=startstr[i]:
                res = False
    else:
        res= False
    return res
# print startWith('#abc','#')

def splitSpace(line):
    return re.split('\s',line)

def addEscapingChar(inputstr):
    res=''
    for i in inputstr:
        if i =='&' or i=='?' or i=='_' or i=='$':
            i='\\'+i
        res+=i
    return res

def pathGetIdx(path):
    idx = path[::-1].find('/')
    if idx!=-1:
        return len(path)-idx
    return -1
    # len(path)-
def pathGetFile(path):
    idx = pathGetIdx(path)
    if idx!=-1:
        return path[idx:]
    else:
        return None

# p='/dataaaa'
# p='dataahaha'
# print pathGetFile(p)
# print p[getLastDirIdx(p):]
