#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import util.common.systemutil as sysu


osname = sysu.getOS()
if osname==sysu.CYGWIN: #or osname==sysu.LINUX:
    ddisk=os.sep+'d'
    projectLocal=ddisk+os.sep+'project'
elif osname==sysu.WINDOWS:
    ddisk='D:'
    projectLocal=ddisk+os.sep+'project'
elif osname==sysu.MAC:
    ddisk='/Users/liujianlong'
    projectLocal = '/opt/projectL'
else:
    raise Exception,'unknow OS!'

yppath=ddisk+os.sep+'yp'
# yp/project
project=yppath+os.sep+'project'
# yp/project/shell
shellprj=project+os.sep+'shell'
# yp/project/shell/bin
shellPrivatePrj=shellprj+os.sep+'bin'
# yp/project/shell/bin/bashrc
privateBashrc=shellPrivatePrj+os.sep+'bashrc'
# projectLocal/shellshare
shellSharePrj=projectLocal+os.sep+'shellshare'
# projectLocal/shellshare/bashrc
bashPathPrefix=shellSharePrj+os.sep+'bashrc'
# yp/project/shell/bashrc/online
onlineBashrc=privateBashrc+os.sep+'online'
# yp/project/shell/bashrc/office
officeBashrc=privateBashrc+os.sep+'office'

# print onlineBashrc
