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

 
	 def function(self,listAll,globalLower):
	 	result = []
	 	accumulatorR = 0.0
	 	accumulatorP = 0.0
	 	for infor in listAll:
	 		for i in range(globalLower):
	 			#accumulatorP+=infor[i].get_r()
	 			#accumulatorR+=infor[i].get_p()	 			
	 			


	 	