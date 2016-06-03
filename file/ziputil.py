# /usr/bin/python
# -*- coding:utf-8 -*-

import util.common.systemutil as sysu
# import util.log.logger as logger

#log = logger.Logger(loglevel=1, logger="stdout").getlog()

import util.log.logutil as logutil
log = logutil.LogUtil.getStdLog()

#(loglevel=1, logger="stdout").getlog()


'''
tar -cvf ...
'''
def tar_ccmd(tarfile,rawfile,show=False,execludes=[]):
    tar_cmd(tarfile,rawfile,show,pack=True,rawexecludes=execludes)

'''
tar -xvf ...
'''
def tar_xcmd(tarfile,rawfile,show=False):
    tar_cmd(tarfile,rawfile,show,pack=False)

'''
[root@www ~]# tar -jcv -f /root/etc.newer.then.passwd.tar.bz2 --newer-mtime="2008/09/29" /etc/*
tar -zxvf xxx.tar.gz -C xxxx
tar -zcvf xxx.tar.gz xxxx
'''
def tar_cmd(tarfile,rawfile,show=False,pack=False,rawexecludes=[],debugSW=False):
    cmd='tar -z'
    if show:
        cmd+='v'
    if pack:
        cmd+='c'
    else:
        cmd+='x'
    cmd+='f '
    cmd+=tarfile+' '
    if pack:
        if isinstance(rawfile,list):
            for rf in rawfile:
                cmd+=rf+' '
        else:
            cmd+=rawfile+' '
    else:
        cmd+='-C '+rawfile+' '
    if rawexecludes:
        for ex in rawexecludes:
            cmd+='--exclude '+ex+' '
    log.debug( 'tar cmd:\n' + cmd )

    ret,datas = sysu.shellExec(cmd,debugLog=debugSW)
    if ret:
        log.info('tar success ')
    else:
        log.info('tar fail ')

# files=['aaa','bbbb']
# tar_cmd('a.tar.gz','aaa',show=True,pack=True)

# tf='/opt/projectL/htest.tar.gz'
# sf='/opt/projectL/htest'
# tar_ccmd(tf,sf,show=True)
# tar_xcmd('a.tar.gz','ccc',show=True)

# exs=['/opt/target','/opt/sdfsd/target']
# tar_ccmd('aaa.tar.gz','xxxx',True,exs)



