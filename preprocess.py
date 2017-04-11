import nltk
import re
import os
from nltk.tokenize import sent_tokenize, word_tokenize
from textblob import TextBlob
from os.path import dirname
from adapt.intent import IntentBuilder


text = raw_input("please enter your question here: ")
text = text.lower()
sent_list = text.split(' ')
thisType = ""
types = ("what", "who", "when", "why", "how")

if(len(sent_list) != 0 and sent_list[0] in types):
    thisType = sent_list[0]
else:
    for word in sent_list:
        if(word in types):
            thisType = word
tb = TextBlob(text)
keyword = tb.noun_phrases

output = []
output.append(thisType)
output.append(" ".join(keyword))

print(output)
