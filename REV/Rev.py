#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
import os
import nltk
import math
from nltk import FreqDist
from ManipulateFile import ManipulateFile
from TextFileDocument import TextFileDocument
from DocumentReference import DocumentReference
from TokenOccurence import TokenOccurence
from TokenInfo import TokenInfo
from TextStringDocument import TextStringDocument

class Rev(object):	

	def serach(self):			
		# CARREGANDO O DICIONARIO DE WORDS
		dictionaryWords = self.retrieve_dictionary()
		dictQuery = {}
		dictDocumentContainsTokensQuery= {}
		query =  input("O que deseja consultar? ")		
		dictStopWords = self.get_stopwords()		

		hashTableVector = TextStringDocument().to_vector(query,dictStopWords)

		documentReference = DocumentReference("query")
		freque_max  =  hashTableVector.max()		
		documentReference.set_max_token(freque_max)		
		for token in hashTableVector.keys():
			freque = hashTableVector.get(token)			
			tokenOccurence = TokenOccurence(documentReference,freque)					
			tokenInfo  = TokenInfo([tokenOccurence])					
			dictQuery[token]=tokenInfo

		#CALCULANDO IDF e TAM DOCUMEN
		for token in dictQuery.keys():
			tokenInfo = dictQuery[token]
			# AQUI SEMPRE VAI SER 
			idf = self.calculation_idf(1,tokenInfo.size_listTokenOccurence())
			tokenInfo.set_idf(idf)
			dictQuery[token] = tokenInfo
			for tokenOccurence in tokenInfo.get_listTokenOccurence():
				tokenOccurence.get_documentReferencedocRef().add_weight(idf)
					
		return self.process(dictQuery,dictionaryWords)		

	def process(self,dictQuery,dictionaryWords):
		r ={}
		for token in dictQuery.keys():
			if token in dictionaryWords:
				tokenInfo = dictionaryWords[token]
				idf = tokenInfo.get_idf()				
				tokeInfoQuery = dictQuery[token]				
				countTokenQuery = tokeInfoQuery.get_listTokenOccurence()[0].get_count()						
				w = idf * countTokenQuery
				listTokenOccurence = tokenInfo.get_listTokenOccurence()
				for tokeInfoQuery in listTokenOccurence:
					count = tokeInfoQuery.get_count()
					documentRef = tokeInfoQuery.get_documentReferencedocRef()
					if not r.__contains__(documentRef):						
						r[documentRef] = 0.0
					else:
						try:
							r[documentRef]+= (w * idf * count)
						except ZeroDivisionError:
							r[documentRef]+= 0.0

		l = 0.0				
		for documentRef in r.keys():
			l+= math.pow(r[documentRef],2)

		l = math.sqrt(l)	
		for documentRef in r.keys():
			s = r[documentRef]
			y = documentRef.length()
			try:
				r[documentRef] = s/(l*y)
			except ZeroDivisionError:
				r[documentRef] = 0 
			
		print(len(r))
		scores = [(k,r[k]) for k in sorted(r, key=r.get,reverse=True)]				      
		return scores


	def calculation_idf(self,numberOfDocuments,df):
		return math.log((float(numberOfDocuments)/float(df)))		

	def retrieve_dictionary(self):
		manipulateFile = ManipulateFile()
		return manipulateFile.read_file("dictionary")

	def get_stopwords(self):			
		stopwords = nltk.corpus.stopwords.words('english')	
		dictStopWords= {}
		for x in stopwords:
			dictStopWords[x]=""
		return dictStopWords



r = Rev()
r.serach()