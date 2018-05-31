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
		accumulatorF = 0.0
		for infor in listScores:
			accumulatorC+= infor[position].get_c()
			accumulatorP+= infor[position].get_p()
			accumulatorF= accumulatorF + infor[position].get_Fmeasure()			
		return (accumulatorC,accumulatorP,accumulatorF)
			
	def calculation_f_measure(self,p,r):
		return 2 / (1/r) + (1/p)

	def interpolation_p(self,p):
		for i in range(0,len(p)):
			k = p[i]
			for w in range(i,len(p)):
				compared = p[w]
				if compared > k:
					k = compared
			p[i] = k
		return p
	
	def precision_r(self,score,k):
		amount = 0
		for i in range(0,k):
			if score[i].get_flag() == 1:
				amount+=1
		return amount/k


	def function(self,listAll):
		resultC = []
		resultP = []		
		resultF = []				
		m = len(listAll)			
		for k in range(60):
			r = self.process_help(k,listAll)						
			resultC.append(r[0]/100)
			resultP.append(r[1]/100)			
			x = r[2]/100
			if x <= 1.0:							
				resultF.append(x)
		return (resultC,self.interpolation_p(resultP),resultF)


	



