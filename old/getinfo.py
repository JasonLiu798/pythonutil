#!/bin/env python
#-*- coding:utf-8 -*-
from util.db.redisCon import *
import re
import util.db.tableutil as tbu
from util.db.dbutil import *
from util.db.sqlgen import *



#redisconns = csv2redis(redisfile)
ruIns = RedisUtil()
dbIns = MySqlUtil()
dbconns = csv2conns(dbfile)
# print conns

def account2uid(account,profile=None):
    '''
    email/nick -crc
    mobile -mobile
    uid -mod
    '''
    phonePattern = re.compile(r'(13|14|15|17|18)\d{9}')
    phoneMatch = phonePattern.match(account)
    #emailPattern = re.compile(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+')
    # email可以带.
    emailPattern = re.compile('(\w)+(\.\w+)*@(\w)+((\.\w{2,3}){1,3})')
    ematch = emailPattern.match(account)
    openidPattern = re.compile(r'[a-zA-Z0-9]{10,50}')
    omatch = openidPattern.match(account)
    # print 'om',omatch
    if phoneMatch:
        tableName = tbu.gettab(tabname='js_users_login_mobile',field=account,method=tbu.MOB)
        sql = 'select * from '+tableName+' where ulm_mobile="'+ account+'"'
        key = 'ulm_uid'
    elif ematch:
        tableName = tbu.gettab(tabname='js_users_login_email',field=account,method=tbu.HASH)
        sql = 'select * from '+tableName+' where ule_email="'+ account+'"'
        key = 'ule_uid'
    elif omatch:
        tableName = tbu.gettab(tabname='js_users_login_openuid',field=account,method=tbu.HASH)
        sql = 'select * from '+tableName+' where ulo_openuid="'+ account+'"'
        key = 'ulo_uid'
    else:
        tableName = tbu.gettab(tabname='js_users_login_nick',field=account,method=tbu.CRC)
        sql = 'select * from '+tableName+' where uln_nick="'+ account+'"'
        key = 'ule_uid'
    uid = -1
    if profile!=None:
        con = dbconns.get(profile)
        # print 'con',con
        res = con.query(sql)
        if res!=None and len(res)>0:
            uid = res[0][key]
    # print 'sql res',res
    return sql,uid

def userinfo(uid,profile=None):
    suid = str(uid)
    userTable = tbu.gettab(tabname='js_users',field=uid)
    userInfoTable = tbu.gettab(tabname='js_users_info',field=uid)
    userAccountTable = tbu.gettab(tabname='js_users_account',field=uid)
    userBindInfoTable = tbu.gettab(tabname='js_users_bind_info',field=uid)
    userAddrTable = tbu.gettab(tabname='js_users_addr',field=uid)
    userCommonConfigTable = tbu.gettab(tabname='js_users_common_config',field=uid)
    sqls = []
    sql = 'select * from '+userTable+' where u_uid='+suid
    sqls.append(sql)
    sql = 'select * from '+userInfoTable+' where ui_uid='+suid
    sqls.append(sql)
    sql = 'select * from '+userAccountTable+' where ua_uid='+suid
    sqls.append(sql)
    sql = 'select * from '+userBindInfoTable+' where ua_uid='+suid
    sqls.append(sql)
    sql = 'select * from '+userAddrTable+' where ua_uid='+suid
    sqls.append(sql)
    sql = 'select * from '+userAddrTable+' where ua_uid='+suid
    sqls.append(sql)
    sql = 'select * from '+userCommonConfigTable+' where '
    # if profile!=None:
    return sqls

def format(l):
    for i in l:
        print i+";"

def redisInfo(profile):
    r = conns[profile]
    KEY_JFSW = 'USER_JF_SEARCH_SWITCH'
    # r.set(KEY_JFSW,'ON')
    r.set(KEY_JFSW,'OFF')
    return KEY_JFSW,r.get(KEY_JFSW)

def getMaxUidSql():
    sql='select max(u_uid) u_uid from js_users'
    sql = generateMultiTab(sql,10,logEnable=False)
    sql = 'select max(u_uid) u_uid from ('+sql+') q'
    return sql

def getMaxUid(profile=None):
    sql = getMaxUidSql()
    print sql
    if profile!=None:
        con = dbconns.get(profile)
        res = con.query(sql)
        if res!=None and len(res)>0:
            uid = res[0]['u_uid']
        return uid
    return None

def getMaxUidRedis(profile):
    rcon = redisconns.get(profile)
    uidkey = 'UID_GUID_JUANPI'
    return rcon.get(uidkey)

def setMaxUidRedis(profile,uid):
    rcon = redisconns.get(profile)
    uidkey = 'UID_GUID_JUANPI'
    return rcon.set(uidkey,uid)

dprofiel='devuser'
dprofile = 'testuser'
rprofile = 'dev118'
rprofile = 'test56'

# rprofile = 'dev19'
# print redisInfo(rprofile)


# print 'res',account2uid(account,dprofile)
# print getMaxUid(dprofiel),getMaxUidRedis(rprofile)

#192.168.143.179 192.168.143.165
# rtestfav='test56fav'
# rcon = redisconns.get(rprofile)

format(userinfo(24138623))




getMaxUid()
















