#!/usr/bin/python3
# -*- coding: utf-8 -*-
class TokenOccurence(object):			
	def __init__(self,documentReferencedocRef,count):
		self.documentReferencedocRef = documentReferencedocRef
		self.count = count		

	def get_documentReferencedocRef(self):
		return self.documentReferencedocRef

	def get_count(self):
		return self.count
			
	def set_documentReferencedocRef(self,documentReferencedocRef):
		self.documentReferencedocRef = documentReferencedocRef

	def set_count(self,count):
		self.count = count		

	