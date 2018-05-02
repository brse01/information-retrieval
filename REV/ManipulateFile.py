import pickle
import os

class ManipulateFile(object):
	def __init__(self):
		pass

	
	def write_file(self,name_file,dictionary):			
		#file = self.openFile(name_file,'wb')					
		file = open(name_file+'.txt','wb')
		pickle.dump(dictionary,file)
		file.close()


	def read_file(self,name_file):
		file = self.openFile(name_file,'rb')					
		dictionary = pickle.load(arqu)
		file.close()
		return dictionary

	def open_file(self,name,operation):
		return open(name,operation)


	def list_all_documents(self):			
		return os.listdir(self.directory)