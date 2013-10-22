# -*- coding:utf-8 -*-

import os.path

import Configs

from Entry.Manager import Manager 

manager = Manager(os.path.dirname(__file__) + '/../TestData')

manager.outputToFrank(Configs.FRANK1_PATH)
manager.dump()
