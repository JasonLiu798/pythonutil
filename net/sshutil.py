#!/usr/bin/env python
# -*- coding:utf-8 -*-

import subprocess
'''
if profile==None or filename==None:
    usage()
    sys.exit()
'''

UP='up'
DOWN='down'

def scp(localfile,uploadfile,user,host,port=22,idfile=None,direction=UP):
    cmd='scp '
    cmd+='-P '+port
    if idfile:
        cmd+=' -i '+idfile+' '
    remote = ' '+user+'@'+host+':'+uploadfile+' '
    if direction==UP:
        print 'UPLOAD......'
        cmd+=localfile+remote
    else:
        print 'DOWNLOAD......'
        cmd+=remote+' '+localfile
    print cmd
    # '''
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        print line
    retval = p.wait()

    if retval!=0:
        log.error('scp fail')
        return False
    else:
        return True
    # '''






