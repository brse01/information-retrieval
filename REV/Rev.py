#!/usr/bin/python3
# -*- coding: utf-8 -*


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
from DocumentReferenceQuery import DocumentReferenceQuery
from Infor import Infor


class Rev2(object):	
	
	#dictionaryWords = retrieve_dictionary()
	dictionaryWords = ManipulateFile().read_file("dictionary")
	directory ="/home/bruno/Área de Trabalho/information-retrieval/cfc/consultas_cfc/"	


	def search(self,file):
		listDocumentQuery = self.list_all_documents()

		sizeCollection = len(listDocumentQuery)		
		parameters =  TextStringDocument(file).to_vector(self.directory,self.dictStopWords)
		#Guardando nome do documento / Lista de documentos relevante para essa consulta
		documentReference = DocumentReference(file,parameters[1])
		#hasTableVector
		hasTableVector = parameters[0]		
		#MAIOR FREQUENCIA DENTRO DO DOCUMENTO DE QUERY
		freque_max = hashTableVector.max()
		documentReference.set_max_token(freque_max)
		for token in hashTableVector.keys():
			freque = hashTableVector.get(token)	
			#frequeNormalize = float(freq/freque_max)
			if token in dictQuery:
				tokenInfo = dictWords[token]					
				tokenOccurence = TokenOccurence(documentReference,freque)
				tokenInfo.set_tokenOccurence_list(tokenOccurence)
				dictWords[token] = tokenInfo															
			else:
				tokenOccurence = TokenOccurence(documentReference,freque)					
				tokenInfo  = TokenInfo([tokenOccurence])					
				dictWords[token]= tokenInfo

		return [process_consultation(dictStopWords,self.dictionaryWords),parameters[1]]

	def process_consultation(self,dictQuery,dictionaryWords):
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
					
		scores = [(k,r[k]) for k in sorted(r, key=r.get,reverse=True)]				      
		return scores



	def list_all_documents(self):			
		return os.listdir("/home/bruno/Área de Trabalho/information-retrieval/cfc/consultas_cfc/")	


	def process_all(self):
		listScores = []
		limite = int(input("Sistema deve indexar quantos arquivos de consultas? "))
		if limite == 0:
			limite = 100
		dictQuery ={}
		cont = 0
		print("|PROCESSANDO|")	
		listDocumentQuery = self.list_all_documents()
		for file in listDocumentQuery:
			cont+=1
			if cont >  limite:
				break

			parameters = self.search(file)			
			#score= parameters[0]
			#listDocumentRelevant = parameters[1]			
			#CHAMAR METODO PARA PROCESSAR R,P			
			listResultScore = self.calculation_cobertura_precisao(parameters)
			#DEPOIS ADICOONAR NA LISTA 
			listScores.append(listResultScore)
		#ESSE 
		print("|FIM|")	
		return listScores	
				
	#[numero do documento,(marcar se é relevante,r,p)]
	#listResultScore = [doc,(relevant,r,p)]
	def calculation_cobertura_precisao(self,parameters):
		listDocRelevant = parameters[1]
		allRelevant = len(listDocRelevant)		
		listResultScore = []
		cont= 0;
		score = parameters[0]
		position = 0
		flag = 0
		for n in score:
			doc = n[0]
			if doc in listDocRelevant:
				cont+=1
				flag = 1			

			r = float(position/allRelevant)
			p = float(position/cont)
			listScores.append(doc,(flag,r,p))		
			position+=1	
			flag = 0				

		return listResultScore
	



