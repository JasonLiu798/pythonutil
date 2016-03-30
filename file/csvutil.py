# /usr/bin/python
# -*- coding:utf-8 -*-

import csv

class Csvutil(object):
    filename=''
    def __init__(self,filename):
        self.filename=filename
    def read(self):
        content = list(csv.reader(file(self.filename, 'rb')))
        res=[]
        if len(content)>0:
            header = content[0]
            for line in content[1:]:
                tmp = {}
                for h,l in zip(header,line):
                    # print h,l
                    tmp[h]=l
                res.append(tmp)
        return res
'''
filename = 'C:\\Users\\Administrator\\Desktop\\a.csv'
cu = Csvutil(filename)
res = cu.read()
print res
'''

sshcsv = '/opt/vm/share/csv/server.csv'
dbcsv = '/opt/vm/share/csv/db.csv'
rediscsv = '/opt/vm/share/csv/redis.csv'


def parseRedis():
    return parseRaw(rediscsv)

def parseDb():
    return parseRaw(dbcsv)

def parseSSH(tgt='dict'):
    servers = parseRaw(sshcsv)
    res = {}
    for s in servers:
        res[s['key']]=s
    return res

def parseRaw(csvfile):
    cu = Csvutil(csvfile)
    res = cu.read()
    return res


