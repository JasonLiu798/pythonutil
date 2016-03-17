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
