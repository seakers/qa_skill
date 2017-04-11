#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import numpy as np
from preprocess import infoExtract
import re
import copy
import sys
os.system("pip install --upgrade gensim")
import gensim
from gensim.models import word2vec
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
indir_pre = os.getcwd() + "/"
#topics = {'atheism':0, 'autos':1, 'graphics':2, 'medicine':3, 'motorcycles':4, 'religion':5, 'space':6}


"""
ratio = training ratio = 0.7
training the model based on the frist 70% of  training text
examine accuracy using the last 30% of training text
"""

"""
ratio = 0.7

def model_train(min_count = 1, size = 3, window = 2):
	
	sentences = ""
	text = ""

	for topic in topics:
		test_dir = indir_pre + "data/spell_checking_task/{}/train_docs".format(topic)
		for root, dirs, filenames in os.walk(test_dir):
			for idx, f in enumerate(filenames):
				if idx < len(filenames) * ratio:
					continue
				text += open(os.path.join(root, f),'r').read()
	
	sentences = preprocess_text(text,"weTrain")
	model = word2vec.Word2Vec(sentences, size = size, min_count = min_count, window = window)

	return model
"""

"""
load the pre-trained model for google word2vec
"""

def model_pretrained():
	#comment out the following line after first launch
	
	os.system("curl -O https://s3.amazonaws.com/mordecai-geo/GoogleNews-vectors-negative300.bin.gz")
	
	model = gensim.models.KeyedVectors.load_word2vec_format(os.getcwd() + "/GoogleNews-vectors-negative300.bin.gz", binary=True)
	

	return model


def question_classify(method = "pretrained"):

	"""
	find out which category the word fits
	"""

	#category: dictionary w/ key = category name, value = words in the category
	category = {}
	category["location"] = []
	category["University"] = []

	category["location"].append("Seattle")
	category["location"].append("San Franscisco")
	category["location"].append("New York")

	category["University"].append("Cornell")
	category["University"].append("Harvard")
	category["University"].append("Yale")
	category["University"].append("MIT")
	category["University"].append("Berkeley")

	def word_cluster_value(wordList, category, method = "pretrained"):

		similarities = []
		maxSim = -sys.maxint
		output = ""
		wordList = wordList[1].split()
		for word in wordList:
			for types in category:
				for element in category[types]:
					if(element == types):
						print(types)
						return types
					try:
						similarities.append(model.similarity(word, element))
					except KeyError:
						pass
				normalized_sim = sum(similarities)/len(similarities)
				similarities = []
				if(normalized_sim > maxSim):
					output = types
					maxSim = normalißzed_sim
		print("Question Classification: "+ output)
		return output

	
	wordList = ""
	while(wordList != "stop"):
		wordList = infoExtract()
		if(len(wordList) == 0 or wordList[1] == 0):
			print("oops! empty! please try again")
			continue
		word_cluster_value(wordList, category)
		
			






model = model_pretrained()
#model1 = model_train(min_count = minimum_count, size = size_, window = window_)
question_classify()












