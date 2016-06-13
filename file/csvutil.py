# /usr/bin/python
# -*- coding:utf-8 -*-

import csv
import util.common.systemutil as su
import util.log.logutil as logutil
log = logutil.LogUtil.getStdLog()

SECTION = 'section'
SEC_DFT = 'default'

class Csvutil( object):
    filename = ''

    def __init__(self, filename):
        self.filename = filename
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
        key:
            v1
        val:
            [map]
                key:config name
                val:config value
    '''
    def read(self):
        content = list(csv.reader(file(self.filename, 'rb')))
        section_dict = {}
        if len(content) > 0:
            header = content[0]
            section_dict_raw = self.separate_section(content[1:])
            if section_dict_raw:
                for key in section_dict_raw:
                    config_list = self.parse_row(section_dict_raw[key], header)
                    section_dict[key] = self.listmap2mapmap(config_list)
        return section_dict

    def listmap2mapmap(self,listmap):
        res = {}
        for i in listmap:
            res[i['key']] = i
        return res
    '''
    parse one row
    '''
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
        cur_section_name = SEC_DFT
        for line in lines:
            #print 'line:',line
            if line[0] == SECTION:
                find_first_section = True
                if line[1]:
                    section_name = line[1]
                else:
                    section_name = SEC_DFT
                # section_dict[section_name] = []
                cur_section_name = section_name
            else:
                config_list = section_dict.get(cur_section_name)
                if not config_list:
                    config_list = []
                config_list.append(line)
                section_dict[cur_section_name]=config_list
        return section_dict


'''
csv files
'''
#ssh csv file
servers_csv = '/opt/vm/share/csv/server.csv'
# online_servers_csv = '/opt/vm/share/csv/serverol.csv'
# ssh_online_servers_for_online_csv='~/bin/server.csv'
#db csv file
macdbcsv = '/opt/vm/share/csv/db.csv'
windbcsv = ''

# winDbCSV = 'D:'+os.sep+
rediscsv = '/opt/vm/share/csv/redis.csv'

'''
section constant
'''
PROF_DEV=SEC_DFT
PROF_OMS='oms'
PROF_OMD='omd'
PROF_OMP='omp'
PROF_OM='om'


'''
parse raw
'''
def parse_raw(csvfile):
    cu = Csvutil(csvfile)
    res = cu.read()
    return res

'''
parse section
'''
def parse_contain_section(csvfile):
    servers = parse_raw(csvfile)
    return servers.keys()


def get_server_sections():
    return parse_contain_section(servers_csv)

# print get_server_sections()

def parse_server(section=None):
    return parse_raw_section(servers_csv, section)

def parse_db(section=None):
    ostype = su.getOS()
    csvfile = macdbcsv
    if not section:
        section = SEC_DFT
    if ostype==su.WINDOWS:
        csvfile = windbcsv
    return parse_raw_section(csvfile,section)

def parse_redis(section=None):
    return parse_raw_section(rediscsv,section)


def parse_raw_section(csvfile,section):
    if not section:
        section = SEC_DFT
    servers = parse_raw(csvfile)
    if not servers:
        raise Exception,'parse csv fail'
    return servers[section]




# parse_contain_section(servers_csv)
# res = parse_server()
# print res
# clu.print_map(res,True)
# print parse_db()
# res = parse_redis()
# print res








