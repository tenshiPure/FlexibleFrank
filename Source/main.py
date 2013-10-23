# -*- coding:utf-8 -*-

import os.path

import Configs

from Entry.Manager import Manager 

manager = Manager(os.path.dirname(__file__) + '/../TestData')

manager.pointSwitch(4, 7)
manager.pointSwitch(6, 8)
manager.dump()
