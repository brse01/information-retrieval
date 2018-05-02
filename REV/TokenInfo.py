#!/usr/bin/python3
# -*- coding: utf-8 -*-
class TokenInfo(object):
	def __init__(self,idf,listTokenOccurence):
		self.idf = idf
		self.listTokenOccurence = listTokenOccurence

	def get_idf(self):
		return self.idf
	
	def get_listTokenOccurence(self):
		return self.listTokenOccurence
	
	def set_idf(self,idf):
		self.idf = idf

	def set_listTokenOccurence(self,listTokenOccurence):
		self.listTokenOccurence = listTokenOccurence

	def set_tokenOccurence_list(self,tokenOccurence):
		self.get_listTokenOccurence().append(tokenOccurence)

	def size_listTokenOccurence(self):
		return len(self.listTokenOccurence)
	
	