#!/bin/env python
#-*- coding:utf-8 -*-

'''
log = Logger(logger="stdout",loglevel=1).getlog()
logger = Logger(logname='out.log', loglevel=1, logger="fox").getlog()

'''
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import logging

class LogUtil(object):
    logger=None
    @staticmethod
    def init():#self):
        LogUtil.logger = Logger(loglevel=1, logger="stdout").getLog()
    @staticmethod
    def getStdLog():
        if not LogUtil.logger:
            LogUtil.init()
        return LogUtil.logger

class Logger(object):
    leveln={1:logging.DEBUG,2:logging.INFO,3:logging.WARN,4:logging.ERROR}
    levels={'debug':logging.DEBUG,'info':logging.INFO,'warn':logging.WARN,'error':logging.ERROR}
    def __init__(self,logger,loglevel,logname=None):
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        #get loglevel
        loglevel = self.logLevelFormat(loglevel)
        if loglevel==None:
            raise NameError,loglevel,' got no loglevel match'
        #file handler
        fh=None
        if logname!=None:
            fh = logging.FileHandler(logname)
            fh.setLevel(logging.DEBUG)
        #stdout handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        if fh!=None:
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)
    def logLevelFormat(self,loglevel):
        return self.leveln.get(loglevel) if self.leveln.get(loglevel)!=None  else self.levels.get(loglevel)
    def getLog(self):
        return self.logger


# logger = Logger(loglevel=1, logger="fox").getlog()
# logger.info('ahha')


