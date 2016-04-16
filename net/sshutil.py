#!/usr/bin/env python
# -*- coding:utf-8 -*-

import util.common.systemutil as sysu

import subprocess
import util.log.logger as logger
log = logger.Logger(loglevel=1, logger="stdout").getlog()

'''
if profile==None or filename==None:
    usage()
    sys.exit()
'''
UP='up'
DOWN='down'

'''
scp without password
'''
def scpNP(localfile,uploadfile,user,host,port=22,idfile=None,direction=UP):
    cmd='scp '
    cmd+='-P '+port
    cmd+=addIdfile(idfile)
    remote = ' '+user+'@'+host+':'+uploadfile+' '
    if direction==UP:
        print 'UPLOAD......'
        cmd+=localfile+remote
    else:
        print 'DOWNLOAD......'
        cmd+=remote+' '+localfile
    print cmd
    # '''
    res = shellExec(cmd)
    return res
    '''
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        print line
    retval = p.wait()

    if retval!=0:
        log.error('scp fail')
        return False
    else:
        return True
    '''

'''
execute ssh with out password
'''
def sshNP(user,host,port=22,idfile=None,execmd=None):
    cmd='ssh '
    cmd+='-p '+port+' '
    cmd+=addIdfile(idfile)
    cmd+=user+'@'+host+' '
    if execmd:
        cmd+="'"+execmd+"'"
    ret,datas = shellExec(cmd)
    if ret:
        return datas
    else:
        return None

'''
batch execute sshNP
'''
def bssh(servers,execmd,nosrvKey=None):
    res = {}
    if servers:
        for key in servers.keys():
            if not isInList(nosrvKey,key):
                server = servers.get(key)
                # log.debug('serv %s ',server
                output = sshNP(server['user'],server['ip'],server['port'],'~/.ssh/id_rsa.jianlong',execmd=execmd)
                res[server['key']]=output
            else:
                log.info('srv %s not execute!' % key)
    return res

def isInList(l,tgt):
    for i in l:
        if i==tgt:
            return True
    return False

def addIdfile(idfile=None):
    res=''
    macIdfile='~/.ssh/id_rsa.jianlong'
    if not idfile:
        return res
    if sysu.MAC == sysu.getOS():
    # if idfile:
        res=' -i '+macIdfile+' '
    return res

def shellExec(cmd):
    # log.info('exec: '+cmd)
    # print 'exec',cmd
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    lines = p.stdout.readlines()
    # print 'type ',type(lines),'lines',lines
    # for line in p.stdout.readlines():
        # print line
    retval = p.wait()
    print 'ret',retval,'res',lines
    if retval!=0:
        log.error('ssh exec %s fail' % cmd)
        return False,None
    else:
        return True,lines



