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