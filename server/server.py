#!/usr/bin/env python3

"""
Copyright (c) 2017  (http://r4m80mrx.github.io/)
"""

import os, sys
import threading, queue
import time
import re
import random

os.system("title EVE BANK Internal Version By Rubb1shK1d Team 20180329")

# print LOGO
global VERSION, TEAM
VERSION = "1.0.0"
TEAM = 'Rubb1shK1d Team Produced'
BANNER = '''\033[01;33m\
 ___________    ____  _______
|   ____\   \  /   / |   ____|      \033[01;37m{\033[01;33m%s\033[01;37m}\033[01;33m
|  |__   \   \/   /  |  |__
|   __|   \      /   |   __|
|  |____   \    /    |  |____
|_______|   \__/     |_______|      \033[0m%s\033[0m\n
''' % (VERSION, TEAM)

print(BANNER)

from core.log import LOGGER
LOGGER.info("load core module successfully")

import core.sqlutils as sqlutils
sqlutils.db_init()

	  
class HelloWorld(object):
    def index(self):
        return str(sqlutils.)
    index.exposed = True

cherrypy.quickstart(HelloWorld())