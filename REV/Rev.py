#!/usr/bin/python3
# -*- coding: utf-8 -*

import re
import os
import math

import matplotlib.pyplot as plt
from ManipulateFile import ManipulateFile
from TextFileDocument import TextFileDocument
from DocumentReference import DocumentReference
from TokenOccurence import TokenOccurence
from TokenInfo import TokenInfo
from TextStringDocument import TextStringDocument
from DocumentReferenceQuery import DocumentReferenceQuery
from Infor import Infor
from GenerateChart import GenerateChart

class Rev(object):	
		
	dictionaryWords = ManipulateFile().read_file("dictionary")
	directory ="/home/bruno/Área de Trabalho/information-retrieval/cfc/consultas_cfc/"			
	globalLower = 1000000

	def search(self,file,sizeCollection,dictStopWords):
		#TROCAR ESSA BUSCA AQUI		
		dictQuery= {}			
		parameters =  TextStringDocument(file).to_vector(self.directory,dictStopWords)
		#Guardando nome do documento / Lista de documentos relevante para essa consulta		
		documentReference = DocumentReference(file)		
		#hasTableVector		
		hashTableVector = parameters[0]						
		#MAIOR FREQUENCIA DENTRO DO DOCUMENTO DE QUERY
		freque_max = hashTableVector.max()
		documentReference.set_max_token(freque_max)
		for token in hashTableVector.keys():
			freque = hashTableVector.get(token)			
			#frequeNormalize = int(freque)/int(freque_max)
			if token in dictQuery:
				tokenInfo = dictQuery[token]					
				tokenOccurence = TokenOccurence(documentReference,freque)
				#tokenOccurence = TokenOccurence(documentReference,frequeNormalize)
				tokenInfo.set_tokenOccurence_list(tokenOccurence)
				dictQuery[token] = tokenInfo															
			else:
				tokenOccurence = TokenOccurence(documentReference,freque)					
				#tokenOccurence = TokenOccurence(documentReference,frequeNormalize)
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
						r[documentRef]+= (w * idf * count)					

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
				r[documentRef] = float(normalize)									
									
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
			if cont > limite:
				break
			#parameters	= [SCORES PARA AQUELA CONSULTA,LISTA DOS RELEVANTES PARA A CONSULTA QUERY]			
			parameters = self.search(file,sizeCollection,dictStopWords)											
			listResultScore = self.calculation_precise_coverage(parameters)
			#lista_final = [x for x in parameters[0] if x not in parameters[1]]
			#DEPOIS ADICOONAR NA LISTA 
			#listScores.append(listResultScore)						
			listScores.append(listResultScore)
		print("|FIM-process_all|")			
		return listScores	
	
	def calculation_precise_coverage(self,parameters):	
		#LISTA COM OS NÚMEROS DOS DOCUMENTOS RELEVANTES PARA A CONSULTA Q
		listDocRelevant = parameters[1]		
		allRelevant = len(listDocRelevant)
		if allRelevant > 20:
			allRelevant= 20

		listResultScore = []
		#listResultScoreC= []
		#listResultScoreP= []
		cont=0
		score = parameters[0]				
		position=1
		flag=0				
		auxSmaller=len(score)						

		if self.globalLower > auxSmaller: 			
			self.globalLower = auxSmaller		
			
		for n in score[0:20]:
			doc = int(n[0].get_path())			
			if doc in listDocRelevant:				
				print("Doc"+str(doc)+" posição>"+str(position))
				cont+=1
				flag=1											
			c = float(cont/allRelevant)			
			try:
				p = float(cont/position)	
			except ZeroDivisionError:
				p=0										
			listResultScore.append(Infor(doc,c,p,flag))			
			#listResultScoreC.append(c)
			#listResultScoreP.append(p)
			position+=1				
			flag=0		
		return listResultScore	
		'''
		print("tam"+str(len(listResultScoreC[0:20])))
		plt.plot(listResultScoreC[0:20],listResultScoreP[0:20],color='orange')
		plt.xlabel("Cobertura")
		plt.ylabel("Precisão")
		plt.title("Precisão Média")
		plt.show()	
		'''		

	def calculation_idf(self,numberOfDocuments,df):
		return math.log((float(numberOfDocuments)/float(df)))		

	def list_all_documents(self):			
		return os.listdir("/home/bruno/Área de Trabalho/information-retrieval/cfc/consultas_cfc/")	

	def process_help(self,position,listScores):
		accumulatorC = 0.0
		accumulatorP = 0.0
		for infor in listScores:
			accumulatorC+= infor[position].get_c()
			accumulatorP+= infor[position].get_p()
		return (accumulatorC,accumulatorP)


	#ERRO ESTÁ AQUI#
	def function(self,listAll):
		resultC = []
		resultP = []
		accumulatorC = 0.0
		accumulatorP = 0.0
		m = len(listAll)			
		for k in range(20):
			r = self.process_help(k,listAll)			
			resultC.append(r[0]/m)
			resultP.append(r[1]/m)

		return (resultC,resultP)


	def interpolation_p(self,p):
		print("interpolation_p> "+str(type(p)))
		for i in range(0,len(p)):
			k = p[i]
			for w in range(0,len(p)):
				compared = p[w]
				if compared > k:
					k = compared
			p[i] = k
		return p






c = Rev()
re=c.function(c.process_all())
#(resultR,resultP)
#c -> Cobertura
#p-> Precisão
c = re[0]
p = re[1]
pk = p[0:20]
print(type(pk))
p_interpolation = c.interpolation_p(pk)

GenerateChart().generate(c[0:20],p_interpolation,"Cobertura","Precisão","Precisão Média")

'''
plt.plot(c[0:20],p[0:20],color='orange')
plt.xlabel("Cobertura")
plt.ylabel("Precisão")
plt.title("Precisão Média")
plt.show()
'''
'''
for k in result:		
	for i in range(len(k)):
		if k[i].get_flag() == 1:		
			print('Documento: '+str(k[i].get_doc())+' É RELEVANTE> '+ str(k[i].get_flag()) + ' Relevancia do documento '+ str(k[i].get_r()))
#'''