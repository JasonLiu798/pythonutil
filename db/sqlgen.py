#!/bin/env python
#-*- coding:utf-8 -*-

'''
pip install sqlparse
'''
import sqlparse
import util.log.logger as logger

log = logger.Logger(loglevel=1, logger="stdout").getlog()

'''
generate split table
@param format
    N:normal sql
        SELECT * FROM js_users_1 where xxx union all
        SELECT * ...
    H:html sql
        SELECT * FROM js_users_1 where xxx union all</br>
        SELECT * ....

'''

TAGE_BR='</br>'
TAGS_P='<p>'
TAGE_P='</p>'


def getTokens(sql,logEnable=True):
    sql=sqlparse.format(sql, reindent=True, keyword_case='upper')
    parsed = sqlparse.parse(sql)
    # if logEnable:
        # log.debug('parsed %s' % parsed)
    if len(parsed)<=0:
        raise BaseException,'parse result count zero'
    stmt = parsed[0]  # grab the Statement object
    #filter white space
    tokens = filter(lambda x:not x.is_whitespace(),stmt.tokens)
    return tokens


def generateMultiTabOneTab(sql,tabnames,tabnum=10,fmt='N',logEnable=True):
    pass


def generateMultiTab(sql,tabnames=[],tabnum=10,fmt='N',logEnable=True):
    tokens = getTokens(sql)
    if logEnable:
        printStr=''
        for t in tokens:
            printStr+= str(t)+','
        log.debug('token %s' % printStr)
    res=''
    tableNames = getTableName(tokens)

    if len(tokens)>0:
        pre = None
        idx=0
        for i in range(1,tabnum+1):
            for t in tokens:
                tStr = str(t)
                # print '---',tStr
                tableNameAlias = tableNames.get(tStr)
                if isinstance(tableNameAlias,str):
                    t ='%s_%s'%(t,i)
                elif isinstance(tableNameAlias,list):
                    # t ='%s_%s %s_%s'%(tableNameAlias[0],i,tableNameAlias[1],i)
                    t ='%s_%s %s'%(tableNameAlias[0],i,tableNameAlias[1])
                #else:#dict not get,other tokens
                    #if

                # if '.' in tStr:
                    # sep = tStr.split('.')
                    # t = '%s_%s.%s' % (sep[0],i,sep[1])
                # log.debug('pre %s,now %s' %(pre,t))
                # pre = t
                # idx+=1
                res+='%s '% t
            if i!=tabnum:
                res+='union all'
            if fmt=='H':
                res+=TAGE_BR
            res+='\n'
    return res


def getTableName(tokens):
    pre = None
    tableNames={}
    for t in tokens:
        if str(pre) == 'FROM' or str(pre) =='JOIN': #or tablesNames.get(str(pre)) !=None:
            tmp = str(t).split(" ")
            if len(tmp)>1:
                tableNames[str(t)]=tmp
            else:
                tableNames[str(t)]=''
        # log.debug('pre %s,now %s' %(pre,t))
        pre = t
    return tableNames

# res = generateMultiTab(sql,10)
# print 'res\n',res

# if "." in "aaa.dsf":
#     print 'in'


