#!/bin/env python
#-*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import urllib
import urllib2
import json

#long to ip
def long2ip(ip):
    mask = 0xFF
    ip1 = ip & mask         # 0~7
    ip2 = (ip >> 8) & mask  # 8~15
    ip3 = (ip >> 16) & mask # 16~23
    ip4 = (ip >> 24) & mask # 24~31
    l=[str(i) for i in [ip4,ip3,ip2,ip1]]
    ips = '.'.join(l)
    return ips

# l=[2031683355,2104927966,3062488963,455847545,1895469722]
# x=[long2ip(i) for i in l]
# print x

#string to long
def ip2long(ip):
    iplong=ip.split('.')
    # print 'long',iplong
    res = 16777216 * int(iplong[0]) + 65536 * int(iplong[1]) + 256 * int(iplong[2]) + int(iplong[3])
    return res

# l=['121.25.7.27', '125.118.166.222', '182.137.223.131', '27.43.174.121', '112.250.146.154']
# print [ip2long(i) for i in l]


'''
@param ip
    long: 1884992363
    string: 123.123.123.123
@param lib
    S: use ip2locatSina
    T: use ip2locatTaobao
'''
def ip2locat(ip,lib='T'):
    #format ip
    if isinstance(ip,str):
        if ip.isdigit():
            ip=int(ip)
        else:
            sip=ip
            nip=ip2long(ip)
    if isinstance(ip,(int,long)):
        sip=long2ip(ip)
        nip=ip
    # print sip    print nip
    if lib=='S':
        tres=ip2locatSina(sip)
    elif lib=='T':
        tres=ip2locatTaobao(sip)
    else:
        res=''
    print tres
    restr = '|'.join( tres )
    return restr

def ip2locatTaobao(ip):
    url='http://ip.taobao.com/service/getIpInfo.php'
    # url='http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=js'
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2540.0 Safari/537.36'
    headers = { 'User-Agent' :user_agent }
    values = {'ip' : ip}
    data= urllib.urlencode(values)
    req = urllib2.Request(url,data, headers)
    resp = urllib2.urlopen(req)
    respstr = resp.read()
    res = json.loads(respstr)
    raw= res['data']
    return raw.get('country'.encode('utf-8')),raw.get('area'.encode('utf-8')),raw.get('region'.encode('utf-8')),raw.get('city'.encode('utf-8'))

def ip2locatSina(ip):
    url='http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=js'
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2540.0 Safari/537.36'
    headers = { 'User-Agent' :user_agent }
    values = {'ip' : ip}
    data= urllib.urlencode(values)
    req = urllib2.Request(url,data, headers)
    resp = urllib2.urlopen(req)
    respstr = resp.read()
    print respstr
    # print respstr.find('{')
    jdict=json.loads(respstr[respstr.find('{'):respstr.find('}')+1])
    return jdict.get('country'.encode('utf-8')),jdict.get('province'.encode('utf-8')),jdict.get('city'.encode('utf-8'))
    #,jdict.get('district'.encode('utf-8'))

def batchIp2Locate(ips,lib='T'):
    res={}
    i=0
    for ip in ips:
        if i %2:
            res[ip]=ip2locat(ip,'T')
        else:
            res[ip]=ip2locat(ip,'S')
    return res

# res=ip2locatSina('60.172.191.5')
# res= ip2locat('60.172.191.5','T')
res=batchIp2Locate(['121.25.7.27', '125.118.166.222', '182.137.223.131', '27.43.174.121', '112.250.146.154'])
# print res
for i in res:
    print i,res[i]

'''
l=[
1884992363,
1884992363,
3056414827,
1932446010,
1903858917,
719484869,
1964667808,
1018353640,
1018353621,
466486439,
2003186340,
18548142,
2032085746,
1928930620,
1928930620,
236122985,
455847545,
3084813916,
3084813916,
1017954053,
]

s = set([])
for i in l:
    s.add(i)
print s

# for i in s:
    # print 'i',ip2locat(i)
res= ip2locat('1017954053')
print 'res',res

'''



