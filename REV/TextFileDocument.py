#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
import os
import nltk
import FileDocument
from nltk import FreqDist

class TextFileDocument(object):	
	def __init__(self, url_document):
		self.url_document = url_document

	def to_vector(self,path):		
		file =open(path+self.url_document,'r', encoding='utf-8');
		words = file.read()							
		file.close()
		stemmer = nltk.stem.RSLPStemmer()
		words = re.sub('[^A-Za-z]+',' ',words)				
		#DEIXANDO TODAS MINUSCULAS
		words = words.lower()								
		word_tokenize = nltk.word_tokenize(words)								
		resultTokenize = []
		dictStopWords = self.get_stopwords()
		for toke in word_tokenize:
			toke = stemmer.stem(toke)				
			if not dictStopWords.__contains__(toke): 
				resultTokenize.append(toke)			
		#hasTableVector		
		return FreqDist(resultTokenize)	


	def get_stopwords(self):			
		stopwords = nltk.corpus.stopwords.words('english')	
		dictStopWords= {}
		for x in stopwords:
			dictStopWords[x]=""
		return dictStopWords


