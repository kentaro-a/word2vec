# -*- coding: utf-8 -*-


"""
	Class of Using Word2vec.
		- author: kentaro-a
		- created: 2016/12/16
"""
import os, sys, MeCab, csv
from gensim.models import word2vec
from datetime import datetime

class Word2vec:

	"""
		Initialize
	"""
	def __init__(self):
		self._tmpdir = self.getDatePfx() + "_tmp"
		os.mkdir(self._tmpdir)


	"""
		Clean up.
	"""
	def clearTempFiles(self):
		if "_tmpdir" in self.__dict__:
			import shutil
			shutil.rmtree(self._tmpdir)


	"""
		Date prefix for filename, etc...
	"""
	def getDatePfx(self, fmt="%Y%m%d%H%M%S"):
		return datetime.now().strftime(fmt)


	"""
		分かち書き
	"""
	def sepWordBySpace(self, input):
		ret = ''
		tagger = MeCab.Tagger('-Owakati')
		fi = open(input, 'r')
		line = fi.readline()
		while line:
			ret += tagger.parse(line)
			line = fi.readline()
		fi.close()

		self._separatedText = ret
		self._separatedTextPath = self._tmpdir + "/" + self.getDatePfx() + "_septextfile"
		fo = open(self._separatedTextPath, 'w')
		fo.write(self._separatedText)
		fo.close()

		return self



	"""
		Create Word2vec model.
	"""
	def createModel(self, usr_params={}):

		params = {
					'sg': 1,
					'size': 100,
					'min_count': 1,
					'window': 10,
					'hs': 1,
					'negative': 0
				}
		params.update(usr_params)
		sentences = word2vec.LineSentence(self._separatedTextPath)
		self._model = word2vec.Word2Vec(sentences, **params)
		return self



	"""
		Save model.
	"""
	def saveModel(self, modelfilename):
		if "_model" in self.__dict__:
			self._model.save(modelfilename)
		return self


	"""
		cos類似度取得
	"""
	def getCosSimilarities(self, posword, negword=[], topn=10):
		model = self.getModel()
		self._result = model.most_similar(positive=posword, negative=negword, topn=topn)
		return self


	"""
		cos類似度取得
	"""
	def getCosSimilaritiesByFile(self, modelfilepath, posword, negword=[], topn=10):
		model = word2vec.Word2Vec.load(modelfilepath)
		self._result = model.most_similar(positive=posword, negative=negword, topn=topn)
		return self


	"""
		To Csv
	"""
	def toCsv(self, csvname):
		ret = self.getResult()
		csvStr = ''
		f = open(csvname, 'w')
		writer = csv.writer(f, lineterminator='\n')
		writer.writerows(ret)
		f.close()
		return self







	"""
		Getters
	"""
	# 分かち書き後のtextを返す
	def getSeparatedText(self):
		return self._separatedText

	# model object
	def getModel(self):
		return self._model

	# result
	def getResult(self):
		return self._result
