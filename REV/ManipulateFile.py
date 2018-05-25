import pickle
import os

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
	
	#CAPITURAR APENAS AS LINHAS DE PESQUISAS DENTRO DOS DOCUMENTOS DE PESQUISAS
	def filter_text_query(self,path):
		lines= []		
		file =open(path+self.url_document,'r', encoding='utf-8');				
		for line in file:
			line = line.replace('\n','')
			if "RD" in line:
				file.close()									
				return lines[1:len(lines)-1]
			else:
				lines.append(line)	

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
			if aux == 1:
				docs = docs + " " + text[i][4:]
		result_docs = ""
		for i in range(0,len(docs)):
			if docs[i] != " " and aux % 2 != 0:
				result_docs = result_docs + docs[i]
			else:
				if docs[i] == " " and i+1 < len(docs) and docs[i+1] != " ":
					result_docs = result_docs + " "
					aux = aux + 1
		result_docs = result_docs.replace("  ", " ")
		docs = result_docs.strip().split(" ")
		result_docs = []
		for doc in docs:
			#result_docs.append(int(doc))
			print(doc)
			result_docs.append(doc)
		return result_docs



