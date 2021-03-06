# -*- coding:utf-8 -*-

import os.path

from Parts.Id import Id
from Parts.Type import Type
from Parts.Extension import Extension
from Parts.Depth import Depth
from Parts.Path import Path
from Parts.Name import Name
from Parts.Point import Point
from Parts.Output import Output

class Entry:

	ROOT_PATH = None

	#
	# 初期化
	#
	@staticmethod
	def initialize(rootPath):
		Entry.ROOT_PATH = os.path.abspath(rootPath)
		Id.initialize()
		Point.initialize()

	#
	# コンストラクタ
	#
	def __init__(self, type, fullPath):
		self.id = Id()
		self.type = Type(type)
		self.path = Path(fullPath)
		self.depth = Depth(Entry.ROOT_PATH, fullPath)
		self.name = Name(fullPath)
		self.point = Point()
		self.extension = Extension(fullPath)
		self.output = Output(self.point, self.depth, self.name, self.type)

	#
	# 再帰的ループ
	#
	def loop(self):
		return self.generator(self)

	#
	# イテレータ
	#
	def __iter__(self):
		return iter(self.entries)

	#
	# ジェネレータ
	#
	def generator(self, entry):
		yield entry

		if entry.type.isDirectory():
			for subDirectory in entry:
				for subEntry in self.generator(subDirectory):
					yield subEntry 

	#
	# ポイント状態を切り替える
	#
	def pointSwitch(self):
		self.point.switch()

	#
	# デバッグ出力
	#
	def dump(self):
		print ' '
		print self.id
#		print self.type
#		print self.path
#		print self.name
#		print self.depth
#		print self.extension
		print self.point
		print self.output
