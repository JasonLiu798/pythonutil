# /usr/bin/python
# -*- coding:utf-8 -*-

import csv
import util.common.systemutil as su
# import util.log.logger as logger
# log = logger.Logger(loglevel=1, logger="stdout").getlog()
import util.log.logutil as logutil
log = logutil.LogUtil.getStdLog()
import util.common.collectionutil as clu
# import util.log.logger as logger
# log = logger.Logger(loglevel=1, logger="stdout").getlog()

SECTION='section'

class Csvutil(object):
    filename=''
    def __init__(self,filename):
        self.filename=filename
    '''
    file format:
    ```
    f1,f2,f3,....,fn
    section,s1
    v1,v2,v3,....,vn
    ...
    section,s2

    ...
    section,sn
    ...
    ```

    res format:
    [map]
    key:section name
    val:
        [map]
            key:config name
            val:config value
    '''
    def read(self):
        content = list(csv.reader(file(self.filename, 'rb')))
        section_dict = {}
        if len(content)>0:
            header = content[0]
            section_dict_raw = self.separate_section(content[1:])
            if section_dict_raw:
                for key in section_dict_raw:
                    config_list = self.parse_row(section_dict_raw[key],header)
                    section_dict[key] = config_list
        return section_dict

    def parse_row(self,lines,header):
        res = []
        for line in lines:
            tmp = {}
            for h,l in zip(header,line):
                tmp[h]=l
            res.append(tmp)
        return res
    '''
    res format:
    [map]
    key:section name
    val:
        [list] of config
    '''
    def separate_section(self,lines):
        section_dict = {}
        default_section = []
        cur_section_name = 'default'
        for line in lines:
            #print 'line:',line
            if line[0] == SECTION:
                find_first_section = True
                if line[1]:
                    section_name = line[1]
                else:
                    section_name = 'default'
                # section_dict[section_name] = []
                cur_section_name = section_name
            else:
                config_list = section_dict.get(cur_section_name)
                if not config_list:
                    config_list = []
                config_list.append(line)
                section_dict[cur_section_name]=config_list
        return section_dict

#profiles
OL='online_for_online'
OLFL='online_for_local'
LC='local_for_local'
#ssh csv file
servers_csv = '/opt/vm/share/csv/server.csv'
# online_servers_csv = '/opt/vm/share/csv/serverol.csv'
# ssh_online_servers_for_online_csv='~/bin/server.csv'
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
    csvfile=servers_csv
    # if profile==None:
    #     profile=LC
    # if profile==LC:
    #     csvfile=dev_servers_csv
    # elif profile==OL:
    #     csvfile=online_servers_csv
    if csvfile:
        servers = parseRaw(csvfile)
        return servers
        # for s in servers:
            # res[s['key']]=s
    else:
        log.error('parse ssh file fail')
        return None

def parseRaw(csvfile):
    cu = Csvutil(csvfile)
    res = cu.read()
    return res

# res = parseSSH()
# clu.print_map(res,True)











