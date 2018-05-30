#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import nltk
import math

from TextFileDocument import TextFileDocument
from DocumentReference import DocumentReference
from TokenOccurence import TokenOccurence
from TokenInfo import TokenInfo
from ManipulateFile import ManipulateFile
from InforDocument import InforDocument

class Build_index(object):	

	#directory = "/home/bruno/Documentos/RI/information-retrieval/Implementação2/teste/"
	directory ="/home/bruno/Área de Trabalho/information-retrieval/cfc/arquivos_cfc/"	
	# GUARDAR A MAIOR FREQUENCIA DENTRO DO ARQUIVO
	dictDocument = {}	
	
	def create_dict(self):	
		dictStopWords = self.get_stopwords()
		limite = int(input("Sistema deve indexar quantos arquivos? "))
		if limite == 0:
			limite = 1000

		dictWords = {}
		cont = 0
		print("|PROCESSANDO|")	
		listDocument = self.list_all_documents()		
		sizeCollection=len(listDocument)		
		# LISTA DE DOCUMENTOS.		
		for file in listDocument:
			cont += 1
			if cont > limite:
				break
			#self.dictDocument[file] = InforDocument(0.0,0.0)						
			hashTableVector = TextFileDocument(file).to_vector(self.directory,dictStopWords)						
			# LISTA DE TOKENS 
			documentReference = DocumentReference(file)		
			# VERIFICANDO QUEM É O TOKEN COM MAIOR OCORRENCIA.
			freque_max  =  hashTableVector.max()
			documentReference.set_max_token(freque_max)
			for token in hashTableVector.keys():
				freque = hashTableVector.get(token)					
				#frequeNormalize = freque/int(freque_max)
				if token in dictWords:
					tokenInfo = dictWords[token]					
					tokenOccurence = TokenOccurence(documentReference,freque)
					#tokenOccurence = TokenOccurence(documentReference,frequeNormalize)					
					tokenInfo.set_tokenOccurence_list(tokenOccurence)
					dictWords[token] = tokenInfo															
				else:										
					tokenOccurence = TokenOccurence(documentReference,freque)					
					#tokenOccurence = TokenOccurence(documentReference,frequeNormalize)					
					tokenInfo  = TokenInfo([tokenOccurence])					
					dictWords[token]=tokenInfo					

		#CALCULANDO IDF e TAM DOCUMEN
		for token in dictWords.keys():	
			tokenInfo = dictWords[token]				
			idf = self.calculation_idf(sizeCollection,tokenInfo.size_listTokenOccurence())
			tokenInfo.set_idf(idf)
			dictWords[token] = tokenInfo
			# CALCULANDO O TAMANHO DOS DOCUMENTOS			
			for tokenOccurence in tokenInfo.get_listTokenOccurence():
				tokenOccurence.get_documentReferencedocRef().add_weight(idf)
			
		return dictWords		
		
	
	def calculation_idf(self,numberOfDocuments,df):
		return math.log((float(numberOfDocuments)/float(df)))	

	def list_all_documents(self):			
		return os.listdir(self.directory)			
	

	def get_stopwords(self):			
		stopwords = nltk.corpus.stopwords.words('english')	
		dictStopWords= {}
		for x in stopwords:
			dictStopWords[x]=""
		return dictStopWords


build_index = Build_index()
dictWords=build_index.create_dict()
name = "dictionary"

manipulateFile = ManipulateFile()
manipulateFile.write_file(name,dictWords)
print("|Concluido|")	









