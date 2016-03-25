#!/bin/env python
#-*- coding:utf-8 -*-
#
import binascii

# return binascii.crc32(v)
#return '0x%x' % (binascii.crc32(v) & 0xffffffff)

CRC='crc'
MOD='mod'
HASH='hash'
MOB='mobile'

def modtab(field,tabcnt):
    return int(field)%tabcnt+1
def hashtab(field,tabcnt):
    return gethash(field)%tabcnt+1
def crctab(field,tabcnt):
    return binascii.crc32(field)%tabcnt+1
def mobiletab(field,tabcnt):
    suffix=0
    for i in str(field)[-4:]:
        suffix+=int(i)
    return suffix%tabcnt+1

# print mobiletab('13155122526',10)

def gethash(val):
    val = val.upper()
    if len(val)<4:
        length = len(val)
    else:
        length = 4
    l=0
    for i in range(length):
        l+=ord(val[i]) & 0xff
    return l #first four byte ,&0xff

def gettab(field,tabname=None,method=MOD,tabcnt=10):
    mmap={MOD:modtab,HASH:hashtab,CRC:crctab,MOB:mobiletab}
    if tabname==None:
        return str(mmap.get(method)(field,tabcnt))
    else:
        return tabname+'_'+str(mmap.get(method)(field,tabcnt))
'''
example
print gettab('13155122526','js_users_login_mobile','mobile')
print gettab(23434,'js_users','mod')
print gettab('57454996@qq.com','js_users_login_email',HASH)

'''

# print binascii.crc32('test')


