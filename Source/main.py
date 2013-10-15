# -*- coding:utf-8 -*-

import os.path

from Entry.Entry import Entry
from Entry.Directory import Directory
from Entry.File import File

rootPath = os.path.dirname(__file__) + '/../TestData'

Entry.initialize(rootPath)
tree = Directory(rootPath)

for e in tree.loop():
	print e


##for entry in rootDir.loop(lambda entry: 3 == entry.id):
##	pass

##subDir = rootDir.loop(lambda entry: entry.id == 3).next()

#Entry.Entry.initialize(rootPath)
#grepRootDir = Directory.Directory(rootPath, recursive = False)
#for entry in rootDir.loop():
#	grepResult = entry.grep('log', 'is')
#	if not grepResult.isEmpty():
#		file = FileGrep.FileGrep(entry.path, grepResult)
#		print file

##
## 範囲
##
#range = Range(rootDir, '^', '4')
#rootDir.pointsSwitch(range)

##
## ポイント
##
#for e in rootDir.loop():
#	print e
