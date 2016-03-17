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
