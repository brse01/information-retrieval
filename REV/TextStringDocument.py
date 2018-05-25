#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
import os
import nltk
from nltk import FreqDist
from ManipulateFile import ManipulateFile

class TextStringDocument(object):
	def __init__(self, url_document):
		self.url_document = url_document
	

	def to_vector(self,path,dictStopWords):		
		file =open(path+self.url_document,'r', encoding='utf-8');
		word = file.read()									
		file.close()		
		listDocument = ManipulateFile().filter_list_docs(word) 
		query = ManipulateFile().filter_query_document(word)				
		
		stemmer = nltk.stem.RSLPStemmer()				
		words = re.sub('[^A-Za-z]+',' ',query)		
		words = words.lower()		
		word_tokenize = nltk.word_tokenize(words)										
		resultTokenize = []
		for toke in word_tokenize:
			toke = stemmer.stem(toke)				
			if not dictStopWords.__contains__(toke): 
				resultTokenize.append(toke)			
		#hasTableVector
		print("resultTokenize")
		print(resultTokenize)
		freqDist = FreqDist(resultTokenize)
		print("FreqDist")
		print(freqDist)		
		return  (freqDist,listDocument)				
		
		
	def treat_data(self,words):
		stemmer = nltk.stem.RSLPStemmer()				
		word = re.sub('[^A-Za-z]+',' ',words)		
		word = word.lower()		
		word_tokenize = nltk.word_tokenize(word)										
		resultTokenize = []
		for toke in word_tokenize:
			toke = stemmer.stem(toke)				
			if not dictStopWords.__contains__(toke): 
				resultTokenize.append(toke)

		print("resultTokenize")
		print(resultTokenize)
		print("FreqDist")
		freqDist = FreqDist(resultTokenize)
		print(freqDist.keys())

		return freqDist
