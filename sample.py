# -*- coding: utf-8 -*-

from Word2vec import Word2vec

w2b = Word2vec()
params = {
			'sg': 1,
			'size': 10,
			'min_count': 1,
			'window': 10,
			'hs': 1,
			'negative': 0
		}

# 
results = w2b.sepWordBySpace('path/to/inputfile', 'path/to/sepalatedfile to save')\
			.createModel('', params)\
			.getCosSimilarities('your keyword', '', 100)\
			.getResult()

# Or using exist models, like below.
#results = test.getCosSimilarities('your keyword', 'path/to/model', 100).getResult()

for result in results:
	print(result[0], '\t', result[1])


