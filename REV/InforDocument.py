#!/usr/bin/python3
# -*- coding: utf-8 -*-
class InforDocument(object):
	def __init__(self,length,maxToken):
		self.length = length
		self.maxToken = maxToken

	def set_maxToken(self,maxToken):
		self.maxToken = maxToken

	def set_length(self,length):
		self.length = length

	def get_maxToken(self):
		return self.maxToken
	
	def get_length(self):
		return self.maxToken

	def update_length(self,length):
		self.length = get_length() + length


