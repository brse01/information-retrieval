from ManipulateFile import ManipulateFile

class Rev(object):	


	def consulta(self):		
		dictionary = self.retrieve_dictionary()
		q =  input("O que deseja consultar? ")
		
		



	def retrieve_dictionary(self):
		manipulateFile = ManipulateFile()
		return manipulateFile.read_file("dictionary")



r = Rev()
r.consulta()