# /usr/bin/python
# -*- coding:utf-8 -*-

import re
import sys,os
# import util.log.logger as logger
import util.common.stringutil as su
# log = logger.Logger(loglevel=1, logger="stdout").getlog()

import util.log.logutil as logutil
log = logutil.LogUtil.getStdLog()


T_WR_APPEND='a'


#current dir
def cur_file_dir():
     #获取脚本路径
     path = sys.path[0]
     #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
     if os.path.isdir(path):
         return path
     elif os.path.isfile(path):
         return os.path.dirname(path)

def fileExist(file):
    if not exist(file):
        raise Exception,file+'file not exist'
    if not isFile(file):
        raise Exception,file+'not a file'

def dirExist(directory):
    if not exist(directory):
        return False #raise Exception,'dir not exist'
    if not isDir(directory):
        return False
    return True #raise Exception,'not a dir'

def read(file,otype='r',length=-1):
    fileExist(file)
    file_object = open(file,otype)
    try:
        all_the_text = file_object.read()
        log.debug('read from '+file)
        return all_the_text
    finally:
        file_object.close( )

def readLine(fo,linenumber):
    idx=0
    try:
        while True:
            line = fo.readline()
            if idx==linenumber:
                res = line
                break
            if not line:
                break
            idx+=1
    finally:
        f.close()
    return res
'''
def readSpecifiedByte(fileObject,byte):
    f = open(filepath, 'r')
    content=""
    try:
        while True:
            chunk = fileObject.read(byte)
            if not chunk:
                break
            content+=chunk
    finally:
        f.close()
    return content
'''

def getfd(file,otype='r'):
    fileExist(file)
    file_object = open(file,otype)
    return file_object #don't forget close

# otype = 'a'
def write(file,content,otype='w',length=-1):
    # checkFile(file)
    file_object = open(file, otype)
    try:
        file_object.write(content)
        log.debug('write to '+file)
    finally:
        file_object.close()

#read source files from srcs, write to tgt
def readwrite(srcs,tgt):
    content=''
    if isinstance(srcs,str):
        fileExist(srcs)
        content = read(srcs)
    elif isinstance(srcs,list):
        for s in srcs:
            fileExist(s)
            content +=read(s)
    else:
        raise Exception,('srcs',srcs,'unknow type!')
    write(tgt,content,T_WR_APPEND)

'''
check functions
'''
def exist(file):
    return os.path.exists(file)
def isFile(file):
    return os.path.isfile(file)
def isDir(file):
    return os.path.isdir(file)

'''
delete functions
'''
def deleteFile(file):
    if not exist(file):
        return
    else:
        if isFile(file):
            os.remove(file)
            log.info('delete file '+file)

def deleteDir(targetDir):
    for file in os.listdir(targetDir):
        targetFile = os.path.join(targetDir,  file)
        if os.path.isfile(targetFile):
            os.remove(targetFile)
            log.info('delete file '+targetFile)

def datafileParser(file):
    content = read(file)
    lines = content.splitlines()
    lines = filter(lambda x: not su.startWith(x,'#') and len(x)>1,lines)
    # print lines
    # log.debug('lines'+str(lines))
    return lines


def sshDataParser(file):
    lines = datafileParser(file)
    res=[]
    print lines
    for i in lines:
        tmp = {}
        items = su.splitSpace(i)
        tmp["key"] = items[0]
        tmp["ip"] = items[1]
        tmp["port"] = items[2]
        tmp["user"] = items[3]
        tmp["password"] = items[4]
        res.append(tmp)
    return res

def mkdir(dirpath):
    if dirExist(dirpath):
        return True
    os.mkdir(dirpath)
    return True

'''
get last os.sep
example :
    /aa/bb      return bb
    /aa/bb/     return bb
    aa/         return aa
    /aa/bb///    return bb
'''
def getValueAfterLastSep(filepath):
    res=''
    if filepath and isinstance(filepath,str):
        slen = len(filepath)
        #remove last os.sep
        tmpPath = filepath
        while len(tmpPath)>0 and tmpPath[-1]==os.sep:
            tmpPath=tmpPath[0:len(tmpPath)-1]
        if slen<=1:
            return res
        # print 'after filter :',tmpPath
        idx = tmpPath.rfind(os.sep)
        # print 'idx',idx
        if idx>=0:
            res = tmpPath[idx+1:]
        else:
            res=tmpPath
    return res

# print 'res',getSepLast('/aa/bb///')

'''
filename='D:\\yp\\project\\shell\\share\\bashrc\\moba\\.bash_ssh'
print isDir(filename)


filenameb='D:\\yp\\project\\shell\\share\\bashrc\\moba\\.bash_ssh.bak'

c= read(filename)
write(filenameb,c)
'''

