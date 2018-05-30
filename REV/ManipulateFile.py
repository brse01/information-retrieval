import pickle
import os
import nltk
from nltk import FreqDist

class ManipulateFile(object):
	def __init__(self):
		pass

	
	def write_file(self,name_file,dictionary):					
		file = open(name_file+'.txt','wb')
		pickle.dump(dictionary,file)
		file.close()

	def read_file(self,name_file):		
		file = open(name_file+'.txt','rb')
		dictionary = pickle.load(file)
		file.close()
		return dictionary


	def list_all_documents(self):			
		return os.listdir(self.directory)

	#CAPITURAR APENAS O TEXTOS IMPORTANTES DO DOCUMENTOS DE CONSULTAS	
	def filter_text_document(self,words):
		result =""
		word = words.split('\n')
		for i in range(3,len(word)):
			if word[i][:2] == "AU" or word[i][:2] == "TI" or word[i][:2] == "HJ" or word[i][:2]:
				result = result+ word[i][3:]
			else:
				if word[i][:2] == "RF":
					break;
				if word[i][:2] == "SO":
					result = result+ word[i][3:]
		return result
	    
	#METODO DA OK
	#CAPITURAR APENAS AS LINHAS DE PESQUISAS DENTRO DOS DOCUMENTOS DE PESQUISAS			
	def filter_query_document(self,text):
		query_text = text.split("\n")
		query = ""
		for i in range(1,len(query_text)):
			if query_text[i][:2] == "NR":
				break
			else:
				query = query + query_text[i]
		return query[3:]

	#CAPITURAR APENAS OS NÚMEROS DE DOCUMENTOS RELEVANTES DENTRO DE UM DOCUMENTO DE PESQUISA	
	def filter_list_docs(self,text):	
		aux = 0
		docs = ""
		text = text.split("\n")
		for i in range(3,len(text)):
			if text[i][:2] == "RD":
				docs = text[i][4:]
				aux = 1
				continue
			if aux == 1:
				if text[i][4] == " ":
					docs = docs + " " + text[i][4:]
				else:
					docs = docs + " " + text[i][3:]
		result_docs = []
		docs = docs.replace("  "," ")
		docs = docs.replace("  "," ")
		docs = docs.split(" ")		
		docs = docs[1:]
		for i in range(0,len(docs)):
			if i % 2 == 0 and docs[i] != "":
				result_docs.append(int(docs[i]))	
		return result_docs


	def get_stopwords(self):			
		stopwords = nltk.corpus.stopwords.words('english')	
		dictStopWords= {}
		for x in stopwords:
			dictStopWords[x]=""
		return dictStopWords
