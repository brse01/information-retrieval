#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
import os
import nltk
from nltk import FreqDist
class TextStringDocument(object):

	def to_vector(self,word,dictStopWords):
		stemmer = nltk.stem.RSLPStemmer()
		words = re.sub('[^A-Za-z]+',' ',word)				
		#DEIXANDO TODAS MINUSCULAS
		words = words.lower()								
		word_tokenize = nltk.word_tokenize(words)								
		resultTokenize = []
		for toke in word_tokenize:
			toke = stemmer.stem(toke)				
			if not dictStopWords.__contains__(toke): 
				resultTokenize.append(toke)			
		#hasTableVector		
		return FreqDist(resultTokenize)	
		