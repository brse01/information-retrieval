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

class Rev2(object):	

	directory ="/home/bruno/Área de Trabalho/cfc/consultas_cfc/"

	def serach(self):
		dictStopWords = self.retrieve_dictionary()
		limite = int(input("Sistema deve indexar quantos arquivos de consultas? "))
		if limite == 0:
			limite = 100
		dictQuery ={}
		cont = 0
		print("|PROCESSANDO|")	
		listDocumentQuery = self.list_all_documents()
		sizeCollection = len(listDocumentQuery)
		for file in listDocumentQuery:
			cont+=1
			if cont > limite:
				break
			print(file)			
			print(hashTableVector)




	def list_all_documents(self):			
		return os.listdir(self.directory)

	def retrieve_dictionary(self):
		manipulateFile = ManipulateFile()
		return manipulateFile.read_file("dictionary")
c = Rev2()
c.serach()
print("FIMM")