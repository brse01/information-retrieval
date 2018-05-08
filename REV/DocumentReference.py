#!/usr/bin/python3
# -*- coding: utf-8 -*-
class DocumentReference(object):	
	def __init__(self, path):
		self._path = path
		self._length = 0.0
		self._max_token = 0.0
   
	def add_weight(self, w):
		self._length += w ** 2

	def length(self):
		return math.sqrt(self._length)
	
	def set_max_token(self,value):
		self._max_token = value

	def get_max_token(self):
		return self._max_token

