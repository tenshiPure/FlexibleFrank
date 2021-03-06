# -*- coding:utf-8 -*-

class Output:

	#
	# コンストラクタ
	#
	def __init__(self, point, depth, name, type):
		mark = point.createOutputParts()
		tab = depth.createOutputParts()
		name = name.createOutputParts()
		space = type.createOutputParts()

		self.value = mark + tab + name + space

	#
	# フランク出力
	#
	def toFrank(self, file):
		file.write(self.value + '\n')

	#
	# 文字列出力
	#
	def __str__(self):
		return '%-20s : %s' % ('output', self.value)
