#!/usr/bin/python3
# -*- coding: utf-8 -*

class Infor(object):
	def __init__(self,doc,c,p,flag):
		self._doc = doc
		self._c= c
		self._p= p		
		self._flag = flag

	def get_doc(self):
		return self._doc

	def get_c(self):
		return self._c

	def get_p(self):
		return self._p

	def get_flag(self):
		return self._flag

	#FORMA DE FORMATAR A IMPRESSÃO DE TODOS OS DADOS DE UMA CLASSE	
	def __repr__(self):
		return '<Documento: {}\nr: {}\np: {}\nRelevante: {}\n> '.format(self._doc,str(self._c),str(self._p),str(self._flag))



		


	




