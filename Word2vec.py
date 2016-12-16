# -*- coding: utf-8 -*-


"""
	Class of Using Word2vec.
		- author: kentaro-a
		- created: 2016/12/16 
"""
import sys, MeCab
from gensim.models import word2vec
from datetime import datetime

class Word2vec:
	
	"""
		Initialize
	"""
	def __init__(self):
		# Nothing to do...
		pass

	
	"""
		Date prefix for filename, etc...
	"""
	def getDatePfx(self):
		return datetime.now().strftime('%Y%m%d%H%M%S')

	
	"""
		分かち書き
	"""
	def sepWordBySpace(self, input, output):
		ret = ''
		tagger = MeCab.Tagger('-Owakati')
		
		fi = open(input, 'r')
		line = fi.readline()
		while line:
			ret += tagger.parse(line)
			line = fi.readline()
		fi.close()

		fo = open(output, 'w')
		fo.write(ret)
		fo.close()
		
		self._separatedTextPath = output
		return self
	
	
	"""
		Create Word2vec model.
	"""
	def createModel(self, modelfilename, usr_params={}, separatedTextPath=''):
		
		params = {
					'sg': 1,
					'size': 100,
					'min_count': 1,
					'window': 10,
					'hs': 1,
					'negative': 0
				}
		params.update(usr_params)
		
		if separatedTextPath != '':
			sentences = word2vec.LineSentence(separatedTextPath)
		else:
			sentences = word2vec.LineSentence(self.getSeparatedTextPath())

		self._model = word2vec.Word2Vec(sentences, **params)
		"""
		self._model = word2vec.Word2Vec(
				sentences,
				sg=1,
		   		size=100,
		   		min_count=1,
		   		window=10,
		   		hs=1,
		   		negative=0
			)
		"""
		# Save model.
		self._model.save(modelfilename)
		self._modelfilename = modelfilename
		return self


	"""
		cos類似度取得
	"""
	def getCosSimilarities(self, posword, negword,  modelfilepath='', topn=10):
		if modelfilepath != '':
			model = word2vec.Word2Vec.load(modelfilepath)
		else:
			model = self.getModel()

		self._result = model.most_similar(positive=posword, negative=negword, topn=topn)
		return self
		

	"""
		Getters
	"""
	# 分かち書き後のファイルパスを返す
	def getSeparatedTextPath(self):
		return self._separatedTextPath
	# model object
	def getModel(self):
		return self._model
	# modelfilename
	def getModelfilename(self):
		return self._modelfilename
	# result
	def getResult(self):
		return self._result
	

