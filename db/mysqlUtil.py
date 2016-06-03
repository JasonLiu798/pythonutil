#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from mysqlConn import *
import util.file.csvutil as cu

class MySQLUtil(object):
    pool=None
    def __init__(self):
        rawdata = cu.parseDb()
        # print 'init',rawdata
        self.pool = self.raw2conns(rawdata)
    def get(self,key):
        conn = self.pool[key]
        conn.reconnect()
        return conn
    def profiles(self):
        if self.pool:
            return self.pool.keys()
    def raw2conns(self,rawdata):
        if len(rawdata)<=0:
            raise Exception,'db csv null'
        res = {}
        for rd in rawdata:
            conn = Connection(host=rd['ip'],database=rd['db'],user=rd['user'],password=rd['password'])
            res[rd['key']] = conn
        return res

# muIns = MysqlUtil()
# print muIns.pool
# print muIns.profiles()
# conn = muIns.get('2423308')
# print conn.queryf('select * from js_users_1 limit 10')
# print conn.batchQueryf(['select * from js_users_1 limit 1','select * from js_users_2 limit 1'])


