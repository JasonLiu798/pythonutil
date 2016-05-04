# /usr/bin/python
# -*- coding:utf-8 -*-

import csv
import util.common.systemutil as su
# import util.log.logger as logger
# log = logger.Logger(loglevel=1, logger="stdout").getlog()
import util.log.logutil as logutil
log = logutil.LogUtil.getStdLog()

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
#profiles
OL='ol'
LC='lc'
#ssh csv file
sshLocalCsv = '/opt/vm/share/csv/server.csv'
sshOlCsv = '/opt/vm/share/csv/serverol.csv'

#db csv file
macdbcsv = '/opt/vm/share/csv/db.csv'

windbcsv = ''


# winDbCSV = 'D:'+os.sep+
rediscsv = '/opt/vm/share/csv/redis.csv'


def parseRedis():
    return parseRaw(rediscsv)

def parseDb():
    ostype = su.getOS()
    dbcsv = macdbcsv
    if ostype==su.WINDOWS:
        dbcsv = windbcsv
        raise Exception,'no win file'
    return parseRaw(dbcsv)

def parseSSH(profile=None):
    csvfile=None
    if profile==None:
        profile=LC
    if profile==OL:
        csvfile=sshOlCsv
    elif profile==LC:
        csvfile=sshLocalCsv
    if csvfile:
        servers = parseRaw(csvfile)
        print servers
        res = {}
        for s in servers:
            res[s['key']]=s
        return res
    else:
        log.error('parse ssh file fail')
        return None

def parseRaw(csvfile):
    cu = Csvutil(csvfile)
    res = cu.read()
    return res


