#!/usr/bin/python3
# -*- coding: utf-8 -*
'''
VERIFICAR PORQUE A LISTA DO DOCUMENTOS RELEVANTES QUE VEM DO 
DOCUMENTO I DE CONSULTA NÃO É IGUAL A QUE ESTÁ NO É O NÚMEROS
QUE ESTÃO NO ARQUIVO
'''

import re
import os
import math
from ManipulateFile import ManipulateFile
from TextFileDocument import TextFileDocument
from DocumentReference import DocumentReference
from TokenOccurence import TokenOccurence
from TokenInfo import TokenInfo
from TextStringDocument import TextStringDocument
from DocumentReferenceQuery import DocumentReferenceQuery
from Infor import Infor


class Rev(object):	

	
	#dictionaryWords = retrieve_dictionary()
	dictionaryWords = ManipulateFile().read_file("dictionary")
	directory ="/home/bruno/Área de Trabalho/information-retrieval/cfc/consultas_cfc/"	
	

	def search(self,file,sizeCollection,dictStopWords):
		#TROCAR ESSA BUSCA AQUI		
		dictQuery= {}			
		parameters =  TextStringDocument(file).to_vector(self.directory,dictStopWords)
		#Guardando nome do documento / Lista de documentos relevante para essa consulta		
		documentReference = DocumentReference(file)		
		#hasTableVector		
		hashTableVector = parameters[0]		
		#print("| search |")
		#print(parameters)		
		#print(hashTableVector.keys())
		#MAIOR FREQUENCIA DENTRO DO DOCUMENTO DE QUERY
		freque_max = hashTableVector.max()
		documentReference.set_max_token(freque_max)
		for token in hashTableVector.keys():
			freque = hashTableVector.get(token)	
			#frequeNormalize = float(freq/freque_max)
			if token in dictQuery:
				tokenInfo = dictQuery[token]					
				tokenOccurence = TokenOccurence(documentReference,freque)
				tokenInfo.set_tokenOccurence_list(tokenOccurence)
				dictQuery[token] = tokenInfo															
			else:
				tokenOccurence = TokenOccurence(documentReference,freque)					
				tokenInfo  = TokenInfo([tokenOccurence])					
				dictQuery[token]= tokenInfo

			#CALCULANDO IDF e TAM DOCUMEN
		for token in dictQuery.keys():	
			tokenInfo = dictQuery[token]				
			idf = self.calculation_idf(sizeCollection,tokenInfo.size_listTokenOccurence())
			tokenInfo.set_idf(idf)
			dictQuery[token] = tokenInfo
			# CALCULANDO O TAMANHO DOS DOCUMENTOS			
			for tokenOccurence in tokenInfo.get_listTokenOccurence():
				tokenOccurence.get_documentReferencedocRef().add_weight(idf)
					
		#[SCORES PARA AQUELA CONSULTA,LISTA DOS RELEVANTES PARA A CONSULTA QUERY]		
		return [self.process_consultation(dictQuery,self.dictionaryWords),parameters[1]]

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
				normalize = s/(l*y)						
			except ZeroDivisionError:
				normalize = 0

			if normalize > 0.0:					
				r[documentRef] = normalize				
						
		scores = [(k,r[k]) for k in sorted(r, key=r.get,reverse=True)]				      							
		return scores


	def process_all(self):
		listScores = []
		dictStopWords = ManipulateFile().get_stopwords()
		limite = int(input("Sistema deve indexar quantos arquivos de consultas? "))
		if limite == 0:
			limite = 100
		dictQuery ={}
		cont = 0
		print("|PROCESSANDO-process_all|")	
		listDocumentQuery = self.list_all_documents()
		sizeCollection = len(listDocumentQuery)
		for file in listDocumentQuery:
			cont+=1
			if cont >  limite:
				break
			#parameters	= [SCORES PARA AQUELA CONSULTA,LISTA DOS RELEVANTES PARA A CONSULTA QUERY]			
			parameters = self.search(file,sizeCollection,dictStopWords)						
			#score= parameters[0]
			#listDocumentRelevant = parameters[1]			
			#CHAMAR METODO PARA PROCESSAR R,P			
			#print(parameters[1])
			listResultScore = self.calculation_cobertura_precisao(parameters)
			#lista_final = [x for x in parameters[0] if x not in parameters[1]]
			#DEPOIS ADICOONAR NA LISTA 
			listScores.append(listResultScore)		
		print("|FIM-process_all|")	
		return listScores	
				
	#[numero do documento,(r,p,marcar se é relevante)]
	#listResultScore = [doc,(r,p,relevant)]
	def calculation_cobertura_precisao(self,parameters):
		#LISTA COM OS NÚMEROS DOS DOCUMENTOS RELEVANTES PARA A CONSULTA Q
		listDocRelevant = parameters[1]		
		allRelevant = len(listDocRelevant)		
		listResultScore = []
		cont= 0;		
		score = parameters[0]				
		position = 1
		flag = 0		
		for n in score:
			doc = int(n[0].get_path())			
			if doc in listDocRelevant:				
				cont+=1
				flag=1

			r = float(position/allRelevant)
			try:
				p = float(position/cont)	
			except ZeroDivisionError:
				p=0							
			listResultScore.append(Infor(doc,r,p,flag))
			position+=1	
			flag = 0							
		return listResultScore
	

	def calculation_idf(self,numberOfDocuments,df):
		return math.log((float(numberOfDocuments)/float(df)))		

	def list_all_documents(self):			
		return os.listdir("/home/bruno/Área de Trabalho/information-retrieval/cfc/consultas_cfc/")	
	
			
c = Rev()
result= c.process_all()
print(result)
