# -*- coding: utf-8 -*-

from Word2vec import Word2vec

w2v = Word2vec()
params = {
			'sg': 1,
			'size': 10,
			'min_count': 100,
			'window': 10,
			'hs': 1,
			'negative': 0
		}

# If you have only plain-text as input file, like this.

w2v.sepWordBySpace("path to inputfile")\
	.createModel(params)\
	.getCosSimilarities("your keyword", topn=number-of-rows)\
	.toCsv("path to any csvfile.")\
	.clearTempFiles()
