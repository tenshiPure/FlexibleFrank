# -*- coding:utf-8 -*-

import os.path

import Configs

from Entry.Entry import Entry
from Entry.Directory import Directory
from Entry.File import File


def createTree():
	rootPath = os.path.dirname(__file__) + '/../TestData'
	Entry.initialize(rootPath)
	return Directory(rootPath)

def outputToFrank(tree, filePath):
	frank1 = open(filePath, 'w')
	[entry.output.toFrank(frank1) for entry in tree.loop()]
	frank1.close()

tree = createTree()
outputToFrank(tree, Configs.FRANK1_PATH)
