# -*- coding: utf-8 -*-
#Copyright (C) 2008 Fábio Cerqueira

import xml.dom.minidom

class BoxXML:
	
	def __init__(self,file):
		self._file = file

	def getInfoMap(self,idMap,info):
		"""Método que pega a informações dos maps de acordo com idMap e a info desejada"""
		arq = xml.dom.minidom.parse(self._file)
		for m in arq.getElementsByTagName('map'):
			if int(m.getAttribute('id')) == idMap:
				return m.getElementsByTagName(info)[0].childNodes[0].data