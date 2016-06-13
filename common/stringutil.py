#!/bin/env python
#-*- coding:utf-8 -*-


import sys
reload(sys)
sys.setdefaultencoding('utf8')

import re
import os

def convert_CN(s):
    return s.encode('utf-8')

'''
string start with 'startstr'
    return True
not
    return False
'''
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




def removeLineSepInner(line):
    CR="\r"
    CRCL="\r\n"
    CL="\n"
    res=''
    if line.rfind(os.linesep):
        rstr = re.compile(os.linesep)
        res = rstr.sub('',line)
        # print 'inner:',line,'res:',res
    '''
    elif line.rfind(CR):
        print 'CR'
        res=line.replace(CR, '')
    elif line.rfind(CL):
        print 'CL'
        res=line.replace(CL, '')
    '''
    return res


'''
remove \n \r \n\r
'''
def removeLineSep(line):
    if isinstance(line,str):
        res = removeLineSepInner(line)
    elif isinstance(line,list):
        res=[]
        for l in line:
            res.append(removeLineSepInner(l))
    return res



'''
split by space
'''
def splitSpace(line):
    return re.split('\s',line)


'''
for command  expect
add \\ in front of special character
'''
def addEscapingChar(inputstr):
    res=''
    for i in inputstr:
        if i =='&' or i=='?' or i=='_' or i=='$':
            i='\\'+i
        res+=i
    return res

'''
get / index
'''
def pathGetIdx(path):
    idx = path[::-1].find('/')
    if idx!=-1:
        return len(path)-idx
    return -1

'''

'''
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
