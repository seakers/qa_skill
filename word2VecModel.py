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
	dir = os.getcwd()+"/data"
	for root, dirs, filenames in os.walk(dir):
		for f in filenames:
			with open(dir + "/" + f) as fcontent:
				category[f] = []
				#content = list of example questions
				content = fcontent.readlines()
				for i in xrange(0,len(content)):
					content[i] = content[i].rstrip()
					j=0
					while j <len(content[i]):
						if(not content[i][j].isalpha() and content[i][j] != " "):
							content[i] = content[i][0:j] + content[i][j+1:len(content)]
						else:
							j += 1
				category[f] = content


	def word_cluster_value(wordList, category, method = "pretrained"):
		similarities = []
		maxSim = - sys.maxint
		output = ""
		sentence = wordList[2].split()
		for types in category:
			for part in category[types]:
				for word in sentence:
					tampPart = part.split()
					for element in tampPart:
						#print(word + " " + element)
				#if(element == types):
				#	print(types)
				#	return types
						try:
							similarities.append(model.similarity(word, element))
						except KeyError:
							pass
				if(len(similarities) == 0):
					continue
				normalized_sim = sum(similarities)/len(similarities)

				similarities = []
				if(normalized_sim > maxSim):
					output = types
					maxSim = normalized_sim
		if(len(output) == 0):
			print("sorry, we cannot classify this input at this moment, try another one?")
		print("Question Classification: "+ output)
		return output

	
	wordList = ""
	while(wordList != "stop"):
		wordList = infoExtract()
		if(len(wordList) == 0 or wordList[1] == 0 or wordList[2] == 0):
			print("oops! empty! please try again")
			continue
		word_cluster_value(wordList, category)



#model1 = model_train(min_count = minimum_count, size = size_, window = window_)
model = model_pretrained()
question_classify()












