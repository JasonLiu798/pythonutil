#!/usr/bin/env python


from util.db.mysqlUtil import *
import util.file.fileutil as fu
import urllib


absParentPath = 'D:\\project\\aa'


# dbIns = MySQLUtil('sit','cn:3306','','at','passwd123')
# dbIns.add('dev','10.202.125.245:3306','','as','s')

# sitConn = dbIns.get('sit')
# devConn = dbIns.get('dev')

jsName = 'main'
jsVersion = '0516'
jsContent = fu.read(absParentPath+'main.js')
print 'jsName %s ver %s contentlen %d' % (jsName,jsVersion,len(jsContent))
jsContent = 'aa'

url = "http://10.118.12.118:1080/content/mgr/upd"

body_value = {"type": "J","name": jsName, "version": jsVersion,"content": jsContent }
body_value  = urllib.urlencode(body_value)
request = urllib2.Request(url, body_value)
# request.add_header(keys, headers[keys])
result = urllib2.urlopen(request ).read()
print result



# jsDict1 = {}
# jsDict={}
# jsDict['CNAME'] = jsName
# jsDict['CVERSION'] = jsVersion
# jsDict['CTYPE'] = 'J'
# jsDict['CONTENT'] = 'c'
# jsDict1['datas'] = jsDict

#sitConn.insert('ts_content',jsDict1)

sitConn.execute("insert into ts_content (CNAME,CTYPE,CVERSION,CONTENT) VALUES (%s,%s,%s,%s)",
	jsName,'J',jsVersion,jsContent
	)

# cssName = 'main'
# cssVersion = '0516'
# cssContent = fu.read(absParentPath+'main.css')

# print 'cssName %s ver %s contentlen %d' % (cssName,cssVersion,len(cssContent))


# jsSql = 'insert into ts_content (CNAME,CTYPE,CVERSION,CONTENT) VALUES ({0},{1},{2},{3})'.format(jsName,'J',jsVersion,jsContent)

# cssSql = 'insert into ts_content (CNAME,CTYPE,CVERSION,CONTENT) VALUES ({0},{1},{2},{3})'.format(cssName,'C',cssVersion,cssContent)

# sitConn.execute(jsSql)
# sitConn.execute(cssSql)






















