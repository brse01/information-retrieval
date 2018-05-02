#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import math
from TextFileDocument import TextFileDocument
from DocumentReference import DocumentReference
from TokenOccurence import TokenOccurence
from TokenInfo import TokenInfo
from ManipulateFile import ManipulateFile
from InforDocument import InforDocument

class Build_index(object):	

	directory = "/home/bruno/Documentos/RI/information-retrieval/Implementação2/teste/"
	# GUARDAR A MAIOR FREQUENCIA DENTRO DO ARQUIVO
	dictDocument = {}	
	
	def create_dict(self):	
		dictWords = {}
		print("|PROCESSANDO|")	
		listDocument = self.list_all_documents()		
		sizeCollection=len(listDocument)
		# LISTA DE DOCUMENTOS.
		for file in listDocument:
			self.dictDocument[file] = InforDocument(0.0,0.0)			
			hashTableVector = TextFileDocument(file).to_vector(self.directory)
			# LISTA DE TOKENS 
			documentReference = DocumentReference(file)	
			print("File"+"- "+file)						
			print(documentReference.get_path())
			print(documentReference)
			print("====================")		
			for token in hashTableVector.keys():
				freque = hashTableVector.get(token)								
				if token in dictWords:
					tokenInfo = dictWords[token]					
					tokenOccurence = TokenOccurence(documentReference,freque)
					tokenInfo.set_tokenOccurence_list(tokenOccurence)
					dictWords[token] = tokenInfo										
					#dictWords[token].set_tokenOccurence_list(tokenOccurence)
				else:										
					tokenOccurence = TokenOccurence(documentReference,freque)					
					tokenInfo  = TokenInfo(0.0,[tokenOccurence])					
					dictWords[token]=tokenInfo					

		#CALCULANDO IDF
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

	#Calculando o max{token} no Documento T	
	def update_max_freque_document(self,freque,file):
		if file in self.dictDocument:
			if freque > self.dictDocument[file].get_maxToken():
				inforDocument = self.dictDocument[file]
				inforDocument.set_maxToken(freque)
				self.dictDocument[file] = inforDocument						
		else:					
			self.dictDocument[file] = InforDocument(0.0,freque)				
			

	def write_dict():
		pass


build_index = Build_index()
dictWords=build_index.create_dict()
name = "dictionary"

manipulateFile = ManipulateFile()
manipulateFile.write_file(name,dictWords)










