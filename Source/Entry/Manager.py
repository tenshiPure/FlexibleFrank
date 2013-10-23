# -*- coding:utf-8 -*-

from Entry import Entry
from Directory import Directory
from File import File

class Manager():

	#
	# コンストラクタ
	#
	def __init__(self, rootPath):
		self.tree = self.createTree(rootPath)

	#
	# ファイルツリー作成
	#
	def createTree(self, rootPath):
		Entry.initialize(rootPath)
		return Directory(rootPath)

	#
	# ファイルツリーをフランク出力
	#
	def outputToFrank(self, frankPath):
		frank = open(frankPath, 'w')
		[entry.output.toFrank(frank) for entry in self.tree.loop()]
		frank.close()

	#
	# ファイルツリーの範囲選択
	#
	def inRange(self, entry, first, last):
		if first <= entry.id.value <= last:
			return True

	#
	# 指定エントリのポイントを切り替え
	#
	def pointSwitch(self, first, last):
		[entry.pointSwitch() for entry in self.tree.loop() if self.inRange(entry, first, last)]

	#
	# ファイルツリーをデバッグ出力
	#
	def dump(self):
		[entry.dump() for entry in self.tree.loop()]
