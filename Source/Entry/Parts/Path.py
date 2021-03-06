# -*- coding:utf-8 -*-

import os.path

class Path:

	#
	# コンストラクタ
	#
	def __init__(self, path):
		self.value = os.path.abspath(path)

	#
	# 出力整形用
	#
	def createOutputParts(self):
		return self.value

	#
	# 文字列出力
	#
	def __str__(self):
		return '%-20s : %s' % ('path', self.value)
