#!/usr/bin/env python
#-*- coding:utf-8 -*-

import util.file.fileutil as fu
import util.common.systemutil as sysu
import os
# import util.db.dbutil as du
from filepaths import *
import util.common.stringutil as stru
import util.file.csvutil as cu
from filepaths import *


mobaProfile='moba'
linuxProfile='linux'
macProfile='mac'

#shell/share/bashrc/moba
mobaBashPath=bashPathPrefix+os.sep+mobaProfile

macBashPath=bashPathPrefix+os.sep+macProfile
#shell/share/bashrc/linux
linuxBashPath=bashPathPrefix+os.sep+linuxProfile


#datadir
datadir=shellPrivatePrj+os.sep+'data'
redisData=datadir+os.sep+'redis_server.dat'
srvOtherDat=datadir+os.sep+'srv_other.dat'

if osname==sysu.MAC:
    srvOtherDat= datadir+os.sep+'srv_other_mac.dat'

macFiles={
    "tgt":officeBashrc+os.sep+".zshrc",
    "src":{
        "rcraw":macBashPath+os.sep+".zshrc_raw",
        "ssh":officeBashrc+os.sep+'.bash_ssh',
        "alias":macBashPath+os.sep+'.bash_alias',
        "path":officeBashrc+os.sep+'.bash_path_mac'
    }
}

macBashFiles={
    "tgt":officeBashrc+os.sep+".bashrc_mac",
    "src":{
        "rcraw":macBashPath+os.sep+".bashrc_raw",
        "ssh":officeBashrc+os.sep+'.bash_ssh',
        "alias":macBashPath+os.sep+'.bash_alias',
        "path":officeBashrc+os.sep+'.bash_path_mac'
    }
}

mobaFiles={
    "tgt":officeBashrc+os.sep+".bashrc_moba",
    "src":{
        "rcraw":mobaBashPath+os.sep+".bashrc_raw",
        "ssh":officeBashrc+os.sep+'.bash_ssh',
        "alias":linuxBashPath+os.sep+'.bash_alias',
        "path":officeBashrc+os.sep+'.bash_path_moba'
    }
}
homeMobaFiles={
    "tgt":officeBashrc+os.sep+".bashrc",
    "src":{
        "rcraw":mobaBashPath+os.sep+".bashrc_raw",
        "ssh":officeBashrc+os.sep+'.bash_ssh',
        "alias":linuxBashPath+os.sep+'.bash_alias',
        "path":mobaBashPath+os.sep+'.bash_path'
    }
}

onlineFiles={
    "tgt":"/opt/vm/share/.bashrc",
    "src":{
        "rcraw":onlineBashrc+os.sep+".bashrc_raw",
        "ssh":onlineBashrc+os.sep+'.bash_ssh',
        "alias":linuxBashPath+os.sep+'.bash_alias',
        "path":onlineBashrc+os.sep+'.bash_path'
    }
}


OL='ol'
MOBA='moba'
CYG='cygwin'
MAC='mac'
MACBASH='macbash'

def sshline2alias(servers,idfile=None):
    content = ''
    for s in servers:
        if idfile:
            content+='alias '+s['key']+'="ssh -p '+s['port']+' '+s['user']+"@"+s['ip']+' -i '+idfile+'"\n'
        else:
            content+='alias '+s['key']+'="ssh -p '+s['port']+' '+s['user']+"@"+s['ip']+'"\n'
    return content

def generateSSHAlias(profile):
    print 'USEING',profile
    sshOlineData=datadir+os.sep+'srv_ol_xy.dat'
    sshLocalData=datadir+os.sep+'srv_local.dat'
    if profile==OL:
        # content = fu.read(sshOlineData)
        servers = fu.sshDataParser(sshOlineData)
        content = sshline2alias(servers)
        tgtfile = onlineFiles.get("src").get("ssh")
        # print content,type(content)
    elif profile==MOBA or profile==CYG :
        servers = fu.sshDataParser(sshLocalData)
        content = sshline2alias(servers)
        tgtfile = mobaFiles.get("src").get("ssh")
    elif profile==MAC or profile==MACBASH:
        servers = fu.sshDataParser(sshLocalData)
        content = sshline2alias(servers,'~/.ssh/id_rsa.jianlong')
        tgtfile = mobaFiles.get("src").get("ssh")
    else:
        raise Exception,'no profile match'
    fu.deleteFile(tgtfile)
    fu.write(tgtfile,content)
    fu.readwrite(srvOtherDat,tgtfile)

# generateSSHAlias(MOBA)

# fu.redisDataParser(redisData)

def csv2mysqlcmd():
    res = ''
    dbs = cu.parseDb()
    # print dbs
    if dbs and len(dbs)>0:
        for d in dbs:
            hostport = d['ip'].split(":")
            host=hostport[0]
            port=hostport[1]
            passwd=stru.addEscapingChar(d['password'])
            item = 'alias db'+d['key']+"='mysql -h "+host+' -P '+port+' -u '+d['user']+" -p"+passwd+"'"
            res=res+item+'\n'
    return res

def generateBashrc(profile):
    if profile==OL:
        generateSSHAlias(OL)
        files=onlineFiles
    elif profile==MOBA:
        generateSSHAlias(MOBA)
        files=mobaFiles
    elif profile==MAC:
        generateSSHAlias(profile)
        files=macFiles
    elif profile==MACBASH:
        generateSSHAlias(profile)
        files=macBashFiles
    else:
        raise Exception,('not supported profile',profile)
    tgtfile=files.get("tgt")
    srcfiles=files.get("src").values()
    # for i in srcfiles:
        # print i,fu.exist(i)
    fu.deleteFile(tgtfile)
    fu.write(tgtfile,'# .bashrc\n')
    fu.readwrite(srcfiles,tgtfile)
    if profile!=MOBA:
        mysqlalias=csv2mysqlcmd()
        fu.write(tgtfile,mysqlalias,fu.T_WR_APPEND)
    print 'Result in file:',tgtfile


profile=OL
profile=MAC
profile=MOBA
profile=MACBASH
generateBashrc(profile)
# dbs =
# print dbs




# print addEscapingChar(inputstr)
# csvfile='/opt/vm/share/csv/db.csv'
# print 'res-----------',csv2mysqlcmd()



