#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import os
os.system("pip install --upgrade textblob")
import textblob
from textblob import TextBlob
from os.path import dirname
os.system("python -m textblob.download_corpora")


def infoExtract():
	text = ""
	while(len(text) == 0):
		text = raw_input("enter 'stop' to stop the program. please enter your question here: ")

	text = text.lower()
	tb = TextBlob(text)
	if(text == "stop"):
		return "stop"
	sent_list = text.split(' ')
	thisType = ""
	types = ("what", "who", "when", "why", "how", "where")

	if(len(sent_list) != 0 and sent_list[0] in types):
	    thisType = sent_list[0]
	else:
	    for word in sent_list:
	        if(word in types):
	            thisType = word
	keyword = tb.tags
	result = ""
	for tuples in keyword:

		if(tuples[1] in ["NN", "NNP", "NNS", "NNPS", "JJ"]):

			result += "".join(tuples[0])+" "

	output = []
	output.append(thisType)
	output.append(result)

	print("Question Type: " + output[0] + "KeyInfo: ß" + output[1])
	return output
