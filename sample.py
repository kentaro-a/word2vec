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

# If you have only plain-text as input file and you'd like to create new model, like this.
results = w2v.sepWordBySpace('path/to/inputfile', 'path/to/sepalatedfile to save')\
			.createModel('path/to/modelfile to save', params)\
			.getCosSimilarities(['your positive keywords'], ['your negative keywords'], '', 100)\
			.getResult()

# Or using exist models, like below.
#results = w2v.getCosSimilarities(['your positive keyword'], ['your negative keywords'], 'path/to/model', 100).getResult()

for result in results:
	print(result[0], '\t', result[1])


