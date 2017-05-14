#!/bin/env python
#-*- coding:utf-8 -*-
#
import util.db.tableutil as tbu
from util.db.dbutil import *
from util.db.sqlgen import *
import time
import json
import util.file.fileutil as fu

import util.common.dateutil as dateutil

import pickle
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


# cuser = Connection('127.0.0.1:9001','js_member','memberJavaWriter','45Fab#@7%DP@hZUa2be#')

cuser = Connection('192.168.143.233:3306','js_member','js_xiudang','d8F02&c19G?5_b4$5c6$')


'''
cshare = Connection('127.0.0.1:9002','js_xiudang','majorAppReader','7SGuVle6Us3uVIf9#sj!')

def getAddrChild(addr_id):
    sql = 'select * from js_addr_info where addr_pid = %s' % addr_id
    return cshare.query(sql)

# lv1_addr = getAddrChild(1)

def process(addrid,addrs,lv):
    if lv<=3:
        childs = getAddrChild(addrid)
        # print lv,len(childs)
        if childs!=None and len(childs)>0:
            for ai in childs:
                item = {}
                item['lv'] = lv
                item['name'] = ai['addr_info']
                item['pid'] = ai['addr_pid']
                addrs[ai['addr_id']]=item
                process(ai['addr_id'],addrs,lv+1)
        return

file='addr.dat'
addrBasis = {}
process(1,addrBasis,1)
print addrBasis
addrJson = pickle.dumps(addrBasis)
fu.write(file,addrJson,'wb')
'''
# '''

file='addr.dat'
content = fu.read(file,'rb')
addrBasis=pickle.loads(content)


def timeSum(addtime,counter):
    if addtime <dateutil.getMonth(-6):
        counter[3]+=1
    elif addtime >=dateutil.getMonth(-1):
        counter[0]+=1
    elif addtime >=dateutil.getMonth(-2) and addtime <=dateutil.getMonth(-1):
        counter[1]+=1
    elif addtime >=dateutil.getMonth(-3) and addtime <=dateutil.getMonth(-2):
        counter[2]+=1
    else:
        counter[4]+=1


def stat(tableName,addrBasis):
    sql = 'select uad_province,uad_city,uad_town,uad_cdcode,uad_addtime,last_modified,uad_primary from '+tableName+' where uad_status=1 '#limit 100'
    print sql
    start=time.clock()
    addrs =cuser.query(sql)
    end=time.clock()
    costTime = end-start
    print 'query cost %f s' % costTime
    idx,notfindCnt,errCnt=0,0,0
    oneAllMatch,oneNotMatch=0,0
    twoAllMatch,twoMatchOneCanRestore,twoMatchOne,twoErr=0,0,0,0
    thridAllMath,thirdMatchTwoCanRepair,thirdMatchTwo,thridMatchOne,thridErr=0,0,0,0,0
    #         <1 <2 <3  >6
    addMonth=[0,  0, 0,  0, 0]
    changeMonth=[0,  0, 0,  0, 0]
    primaryCnt=0
    # start=time.clock()
    for add in addrs:
        third = addrBasis.get(int(add['uad_cdcode']))
        addtime=dateutil.ts2date(add['uad_addtime'])
        lastModify = add['last_modified']
        normal=False
        if third:
            if third['lv']==2:#只有两级
                prov=addrBasis.get(int(third['pid']))
                if prov['name'] == add['uad_province'] and third['name']==add['uad_city']:#两级相同
                    twoAllMatch+=1
                    normal=True
                else:
                    twoErr +=1
            elif third['lv']==3:
                # print 'lv3'
                city = addrBasis.get(int(third['pid']))
                prov = addrBasis.get(int(city['pid']))
                if prov['name'] == add['uad_province'] and city['name']==add['uad_city'] and third['name']==add['uad_town'] :#三级相同
                    thridAllMath+=1
                    normal=True
                else:
                    thridErr+=1
            else:
                if third['lv']==1:
                    if add['uad_province']==third['name']:
                        oneAllMatch+=1
                        normal=True
                    else:
                        oneNotMatch+=1
                else:
                    errCnt+=1
        else:
            notfindCnt+=1
        if not normal:
            timeSum(addtime,addMonth)
            timeSum(lastModify,changeMonth)
            if add['uad_primary']==1:
                primaryCnt+=1
        idx+=1

    print ''
    print '表',tableName,'总地址数',idx
    print '字典表未找到',notfindCnt
    print '只有一级：一致的',oneAllMatch,'不一致',oneNotMatch
    print '只有两级：一致的',twoAllMatch,'不一致',twoErr
    # print '只有两级：一致的',twoAllMatch,'可修复',twoMatchOneCanRestore,'不好修复',twoMatchOne,'完全错',twoErr
    # print '三级全对',thridAllMath,'两级匹配可修复',thirdMatchTwoCanRepair,'两级匹配不好修复',thirdMatchTwo,'只有一级匹配',thridMatchOne,'都不匹配',thridErr
    print '三级：一致的',thridAllMath,'不一致的',thridErr

    print '错误地址中：为默认地址的',primaryCnt
    print '错误地址中，添加时间统计：<1个月',addMonth[0],'1~2个月',addMonth[1],'2~3个月',addMonth[2],'>6个月',addMonth[3],'其他',addMonth[4]
    print '错误地址中，修改时间统计：<1个月',changeMonth[0],'1~2个月',changeMonth[1],'2~3个月',changeMonth[2],'>6个月',changeMonth[3],'其他',changeMonth[4]
    print '未知错误',errCnt

# i=1
# stat('js_users_addr_'+str(i),addrBasis)

for i in range(1,11):
    stat('js_users_addr_'+str(i),addrBasis)




