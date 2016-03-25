#!/bin/env python
# -*- coding:utf-8 -*-
#
#

from socket import *


HOST = 'localhost'
PORT = 21568
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

try:
    while True:
        data = raw_input('>')
        if data == 'close':
            break
        if not data:
            continue
        tcpCliSock.send(data)
        data = tcpCliSock.recv(BUFSIZ)
        print data
except:
    tcpCliSock.close()
