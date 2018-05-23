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
		
	def to_vector_define(self,path,dictStopWords):
		stemmer = nltk.stem.RSLPStemmer()
		word = self.to_vector_aux(path)
		print(word)
		'''
		words re.sub('[^A-Za-z]+',' ',word)
		words = words.lower()								
		word_tokenize = nltk.word_tokenize(words)								
		print(word_tokenize)'''


	def to_vector_aux(self,path):			
		lines= []			
		lines = self.to_compress_is_to_read(path)
		lines = lines[1:len(lines)-1]
		
		

	def to_compress_is_to_read(self,path):
		lines= []	
		file =open(path+self.url_document,'r', encoding='utf-8');		
		for line in file:
			line = line.replace('\n','')
			if "RD" in line:
				return	lines			
			else:
				lines.append(line)				


def get_stopwords(self):			
	stopwords = nltk.corpus.stopwords.words('english')	
	dictStopWords= {}
	for x in stopwords:
		dictStopWords[x]=""
	return dictStopWords


d = TextStringDocument("12")
directory ="/home/bruno/Área de Trabalho/cfc/consultas_cfc/"
d.to_vector_define(directory,d.get_stopwords())


'''
if "NR" in line:
					print("aqui")
					break 
				else:
					lines.append(line)
			print(lines)
'''			