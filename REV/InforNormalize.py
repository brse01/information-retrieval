#!/usr/bin/python3
# -*- coding: utf-8 -*

class InforNormalize(object):
	def __init__(self,lower):
		self._r= 0.0
		self._p= 0.0
		self._lower= lower

	def get_r(self):
		return (self._r/self._lower)

	def get_p(self):
		return (self._p/self._lower)

	def set_r(self,r):
		self._r +=r

	def set_p(self,):
		self._p +=p