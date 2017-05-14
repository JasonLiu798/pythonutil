#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os,getopt,sys,subprocess
import util.log.logger as logger
import util.net.sshutil as sshu
import util.file.fileutil as fu
import util.file.csvutil as cu
import util.common.systemutil as su
import util.common.stringutil as stru
log = logger.Logger(loglevel=1, logger="stdout").getlog()

servers = cu.parseSSH()
serverKeys=servers.keys()

def usage(srv=None):
    if srv:
        print 'ERROR:profile '+srv+' not find!'
    print '''UPLOAD:
    scp.py -p x19 -f localfile -r /data -u
    scp.py -p x19 -f localfile -u  [default -r=/data]
DOWNLOAD:
    scp.py -p x19 -r /data/remotefile -d
    servers: %s
    ''' % str(serverKeys)
    sys.exit()

#scp.py -p x19 -f filename -u /data
try:
    options,args = getopt.getopt(sys.argv[1:],"p:f:r:ud")#,["help","ip=","port="])
except getopt.GetoptError:
    usage()

localfile=None
profile=None
remotefile='/data'#default upload dir
direction=sshu.UP
for name,value in options:
    if name in ("-h","--help"):
        usage()
        sys.exit()
    if name in ("-f"):
        localfile=value
    if name in ("-p"):
        profile=value
    if name in ("-r"):
        remotefile=value
    if name in ("-u"):
        direction=sshu.UP
    if name in ("-d"):
        direction=sshu.DOWN


#get server ip port etc.
server=servers.get(profile)
if not server:
    usage(profile)

#default value setting
if direction==None:
    usage()
elif direction==sshu.DOWN:
    if remotefile==None:
        usage()
    if localfile==None:
        localfile =stru.pathGetFile(remotefile)
elif direction==sshu.UP:
    if localfile==None:
        usage()
    if remotefile==None:
        remotefile = '/data' #default -u -r /data


osys = su.getOS()
if osys == su.MAC:
    # scp('/opt/projectL/member/pom.xml','/data','work','192.168.143.19','22','~/.ssh/id_rsa.jianlong',UP)
    sshu.scp(localfile,remotefile,server['user'],server['ip'],server['port'],'~/.ssh/id_rsa.jianlong',direction)
    print localfile
else:
    sshu.scp(localfile,remotefile,server['user'],server['ip'],server['port'],direction=direction)


