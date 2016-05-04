#!/usr/bin/env python
#-*- coding:utf-8 -*-

from redisCon import *
#from util.file.csvutil import *
import util.file.csvutil as cu

class RedisUtil(object):
    pool={}
    def __init__(self):
        rawdata = cu.parseRedis()
        if len(rawdata)<=0:
            raise Exception,'config file null!'
        for rd in rawdata:
            self.pool[rd['key']]=RedisConn(host=rd['host'],port=rd['port'],db=rd['db'])

    def get(self,poolkey=None):
        conn = self.pool[poolkey]
        return conn.getConn()
    def getProfils(self):
        return self.pool.keys()
'''
ruIns = RedisUtil()
print ruIns.getProfils()
conn = ruIns.get('devShare')
print conn
#ruIns.get()
'''



'''

def csv2redis(init=True):
    # cu = Csvutil(csvfile)
    # rawdata = cu.read()
    if len(rawdata)<=0:
        raise Exception,' redis csv null'
    if init:
        res = {}
        for rd in rawdata:
            conn = Connection(host=rd['ip'],database=rd['db'],user=rd['user'],password=rd['password'])
            res[rd['key']] = conn
    else:
        res = rd
    return res
class RedisUtil(object):
    SGL=0
    MULTI=1
    ##
    rtype = 0,one db
    config format:
        {host:xxx,port:xxx,db:0(default)}
    rtype = 1,multi db
    config format:
    {
        coname1:{host:xxx,port:xxx,db:0(default)},
        coname2:{host:xxx,port:xxx,db:0(default)}
    }
    ###
    pool={}
    def __init__(self,config):
        if isinstance(config,str):
            #init using config file
            cu = Csvutil(config)
            rawdata = cu.read()
            if len(rawdata)<=0:
                raise Exception,'config file null!'
            elif len(rawdata)==1:
                self.rtype= self.SGL
                self.pool = redis.ConnectionPool(host=rawdata['host'],port=config['port'],db=config['db'])
            else:
                self.rtype = self.MULTI
                for rd in rawdata:
                    self.pool[rd['key']]=redis.ConnectionPool(host=rd['host'],port=rd['port'],db=rd['db'])
        elif isinstance(config,dict):
            #init by dict
            self.rtype = self.SGL
            for c in config:
                if isinstance(c,dict):#multi
                    rtype = self.MULTI
                    break
            if rtype==self.SGL:
                self.rtype= self.SGL
                self.pool = redis.ConnectionPool(host=config['host'],port=config['port'],db=config['db'])
            else:
                self.rtype= 1
                self.pool = {}
                for key in config:
                    # print config[key]
                    self.pool[key]=redis.ConnectionPool(host=config[key]['host'],port=config[key]['port'],db=config[key]['db'])
        else:
            raise Exception,'config type error,dict or str!'

    def getConn(self,poolkey=None):
        conn = None
        if self.rtype == self.SGL:
            conn = redis.Redis(connection_pool=self.pool)
        else:
            conn = redis.Redis(connection_pool=self.pool[poolkey])
        return conn



# def csv2redis(csvfile):
#     rawdata = cu.parseRedis()
#     # cu = Csvutil(csvfile)
#     # rawdata = cu.read()
#     # print rawdata
#     if len(rawdata)<=0:
#         raise Exception,'redis csv null'
#     res = {}
#     for rd in rawdata:
#         redisconn = RedisConn(host=rd['host'],port=rd['port'],db=rd['db'])
#         res[rd['key']] = redisconn.getConn()
#     return res


def csv2redis(init=True):
    # cu = Csvutil(csvfile)
    # rawdata = cu.read()
    if len(rawdata)<=0:
        raise Exception,' redis csv null'
    if init:
        res = {}
        for rd in rawdata:
            conn = Connection(host=rd['ip'],database=rd['db'],user=rd['user'],password=rd['password'])
            res[rd['key']] = conn
    else:
        res = rd
    return res



example
sconfig={'host':"192.168.143.242",'port':6388,'db':0}
su = RedisUtil(sconfig)
sr = su.getConn()
print sr.get('foo')


mconfig={
    "dev":{'host':"192.168.143.242",'port':6388,'db':0},
    "devfav":{'host':"192.168.143.242",'port':6386,'db':0}
}

mu = RedisUtil(mconfig,1)
mr = mu.getConn('dev')
print mr.get('foo')


# pool = redis.ConnectionPool(host='192.168.143.242', port=6388, db=0)
pool = redis.ConnectionPool(config['dev'])
r = redis.Redis(connection_pool=pool)
# r = redis.StrictRedis(host='192.168.143.242', port=6388, db=0)
#print r.set('foo', 'bar')
print r.get('foo')


ru = RedisUtil('D:\\yp\\project\\python\\data\\redis.csv')
rc = ru.getConn('dev')
print rc.get('foo')
'''




