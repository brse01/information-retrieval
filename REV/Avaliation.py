from InforNormalize import InforNormalize

class Avaliation(object):

	def calculation_precise_coverage(self,parameters):
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


 	#r -> Cobertura
	#p-> Precisã
	 def function(self,listAll,globalLower):	 	
	 	resultC = []
		resultP = []
		accumulatorC = 0.0
		accumulatorP = 0.0	 		 	
		for i in range(20):
			for infor in listAll:
				accumulatorC+=infor[i].get_c()
				accumulatorP+=infor[i].get_p()	 				 			 			 		
			resultC.append((accumulatorC/self.globalLower))
			resultP.append((accumulatorP/self.globalLower))
		return (resultC,resultP)

	 	