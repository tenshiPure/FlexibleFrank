# -*- coding:utf-8 -*-

import os
import os.path

from Entry import Entry
from File import File

from Parts.Type import Type

class Directory(Entry):

	#
	# コンストラクタ
	#
	def __init__(self, fullPath):
		Entry.__init__(self, Type.DIRECTORY, fullPath)
		self.entries = self.getEntries(fullPath)

	#
	# 再帰的にエントリを作成
	#
	def getEntries(self, path):
		entries = []
		for fullPath in [os.path.join(path, entryName) for entryName in os.listdir(path)]:
			if os.path.isfile(fullPath):
				entries.append(File(fullPath))

			if os.path.isdir(fullPath):
				entries.append(Directory(fullPath))

		return entries
