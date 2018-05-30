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

	 def process_help(self,position,listScores):
		accumulatorC = 0.0
		accumulatorP = 0.0
		for infor in listScores:
			accumulatorC+= infor[position].get_c()
			accumulatorP+= infor[position].get_p()
		return (accumulatorC,accumulatorP)
	
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
		for i in range(0,len(p)):
			k = p[i]
			for w in range(0,len(p)):
				compared = p[w]
				if compared > k:
					k = compared
			p[i] = k
		return p

	'''
	def calculate_precision_interpolation_consult(self, precisaoCobertura):
		for i in range(0,len(precisaoCobertura)):
			tuplaI = precisaoCobertura[i]
			for j in range(i,len(precisaoCobertura)):
				tuplaJ = precisaoCobertura[j]
				if tuplaJ[2] > tuplaI[2]:
					tuplaI = (tuplaI[0],tuplaI[1],tuplaJ[2])
			precisaoCobertura[i] = tuplaI #(tuplaI[0],tuplaI[1],tuplaI[2])
		return precisaoCobertura
	'''
	



	 	