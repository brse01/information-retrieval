#!/usr/bin/python3
# -*- coding: utf-8 -*
import matplotlib.pyplot as plt

class GenerateChart(object):

	def generateXY(self,x,y,nameX,nameY,title):
		plt.plot(x,y,color='blue')
		plt.xlabel(nameX)
		plt.ylabel(nameY)
		plt.title(title)
		plt.axis([0,1,0,1])
		#plt.savefig('teste_'+title+'.png') 
		plt.show()
		

	def gerateX(self,x,nameX,title):
		plt.plot(x,color='blue')
		plt.xlabel(nameX)
		plt.ylabel(nameX)
		plt.title(title)		
		plt.show()



		