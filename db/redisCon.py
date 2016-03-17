#!/usr/bin/env python
#-*- coding:utf-8 -*-

import redis
from util.file.csvutil import *

class RedisConn(object):
    def __init__(self, host, port,db ):
        self.host = host
        self.port = port
        self.db = db
    def getConn(self):
        self.pool = redis.ConnectionPool(host=self.host,port=self.port,db=self.db)
        conn = redis.Redis(connection_pool=self.pool)
        return conn

def csv2redis(csvfile):
    cu = Csvutil(csvfile)
    rawdata = cu.read()
    # print rawdata
    if len(rawdata)<=0:
        raise Exception,'redis csv null'
    res = {}
    for rd in rawdata:
        redisconn = RedisConn(host=rd['host'],port=rd['port'],db=rd['db'])
        res[rd['key']] = redisconn.getConn()
    return res
