#-*- coding: utf-8 -*-

import os
import os.path
import sys

def addSys(currentRoot):
	for path in os.listdir(currentRoot):
		fullPath = os.path.join(currentRoot, path)
		if os.path.isdir(fullPath):
			sys.path.append(fullPath)
			addSys(fullPath)



root = os.path.dirname(__file__)
addSys(root)

sys.path = list(set(sys.path))
