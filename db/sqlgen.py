#!/bin/env python
#-*- coding:utf-8 -*-

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
        log.debug('token %s' % tokens)
    res=''
    if len(tokens)>0:
        pre = None
        idx=0
        for i in range(1,tabnum+1):
            for t in tokens:
                if str(pre) == 'FROM' or str(pre) =='JOIN':
                    t='%s_%s'%(t,i)
                # log.debug('pre %s,now %s' %(pre,t))
                pre = t
                idx+=1
                res+='%s '% t
            if i!=tabnum:
                res+='union all'
            if fmt=='H':
                res+=TAGE_BR
            res+='\n'
    return res


# res = generateMultiTab(sql,10)
# print 'res\n',res


