# -*- coding: utf-8 -*-
#Copyright (C) 2008 Fábio Cerqueira

from Map import Map

class Character:
	def __init__(self,map,surf):
		self._map = map #mapa que o personagem faz parte
		self._surf = surf #surface onde o personagem deve ser aplicado
	
	def update(self):
		"""Atualiza o personagem no mapa"""
		self._map.draw(True)
		return self._map.update(self._surf)
		
	def _updateChar(self,mapa,pos):
		"""Método que atualiza no mapa a posição do personagem e a lista de string representativa dele
			mapa: Nova lista de string representativa 
			pos: Nova posição
		"""
		self._map._str = mapa
		self._map._pos = pos
		self.update()
		
	def up(self):
		#copias para facilitar o trabalho
		map = self._map 
		mapt = map._str
		x,y = ax,ay = map._pos
		
		np = x + (y-1) * (map._ssize[0] +1) #pega a posicao de cima na string
		nnp = x + (y-2) * (map._ssize[0] +1) #pega a posicao de cima do acima na string
		
		#transforma o mapa em um string linear.
		sMap = list('\n'.join(map._str))
		
		#movimento permitidos... 
		
		if sMap[np] == '0':  #piso
			y -= 1
			
		elif sMap[np] == '.': #ponto
			y -= 1
			
		elif sMap[np] == '!': #caixa livre
			if sMap[nnp] in ['0','.']: 
				if sMap[nnp] == '0':
					sMap[nnp] = '!'
				elif sMap[nnp] == '.':
					sMap[nnp] = '*'
				
				sMap[np] = '0'
				y -= 1
		
		elif sMap[np] == '*': #caixa no ponto
			if sMap[nnp] in ['0','.']: 
				if sMap[nnp] == '0':
					sMap[nnp] = '!'
				elif sMap[nnp] == '.':
					sMap[nnp] = '*'
				
				sMap[np] = '.'
				y -= 1
		
		#atualiza as infos no mapa
		s = ''.join(sMap).split('\n')
		self._updateChar(s,(x,y))
		return  map.checkFinalize(),(mapt,(ax,ay))
		
	
		
	def down(self):
		#copias para facilitar o trabalho
		map = self._map 
		mapt = map._str
		x,y = ax,ay = map._pos
		
				
		np = x + (y+1) * (map._ssize[0] +1) #pega a posicao de baixo na string
		nnp = x + (y+2) * (map._ssize[0] +1) #pega a posicao de baixo do abaixa na string
		
		#transforma o mapa em um string linear.
		sMap = list('\n'.join(map._str))
		
		#movimento permitidos... 
		
		if sMap[np] == '0':  #piso
			y += 1
			
		elif sMap[np] == '.': #ponto
			y += 1
			
		elif sMap[np] == '!': #caixa livre
			if sMap[nnp] in ['0','.']: 
				if sMap[nnp] == '0':
					sMap[nnp] = '!'
				elif sMap[nnp] == '.':
					sMap[nnp] = '*'
				
				sMap[np] = '0'
				y += 1
		
		elif sMap[np] == '*': #caixa no ponto
			if sMap[nnp] in ['0','.']: 
				if sMap[nnp] == '0':
					sMap[nnp] = '!'
				elif sMap[nnp] == '.':
					sMap[nnp] = '*'
				
				sMap[np] = '.'
				y += 1
		
		#atualiza as infos no mapa
		s = ''.join(sMap).split('\n')
		self._updateChar(s,(x,y))
		return  map.checkFinalize(),(mapt,(ax,ay))
		

	def left(self):
		#copias para facilitar o trabalho
		map = self._map 
		mapt = map._str
		x,y = ax,ay = map._pos
		
				
		np = (x-1) + y * (map._ssize[0] +1) #pega a posicao esq na string
		nnp = (x-2) + y * (map._ssize[0] +1) #pega a posicao de esq do esq na string
		
		#transforma o mapa em um string linear.
		sMap = list('\n'.join(map._str))
		
		#movimento permitidos... 
		
		if sMap[np] == '0':  #piso
			x -= 1
			
		elif sMap[np] == '.': #ponto
			x -= 1
			
		elif sMap[np] == '!': #caixa livre
			if sMap[nnp] in ['0','.']: 
				if sMap[nnp] == '0':
					sMap[nnp] = '!'
				elif sMap[nnp] == '.':
					sMap[nnp] = '*'
				
				sMap[np] = '0'
				x -= 1
		
		elif sMap[np] == '*': #caixa no ponto
			if sMap[nnp] in ['0','.']: 
				if sMap[nnp] == '0':
					sMap[nnp] = '!'
				elif sMap[nnp] == '.':
					sMap[nnp] = '*'
				
				sMap[np] = '.'
				x -= 1
		
		#atualiza as infos no mapa
		s = ''.join(sMap).split('\n')
		self._updateChar(s,(x,y))
		return  map.checkFinalize(),(mapt,(ax,ay))
		
		
	def right(self):
		#copias para facilitar o trabalho
		map = self._map 
		mapt = map._str
		x,y = ax,ay = map._pos
		
		np = (x+1) + y * (map._ssize[0] +1) #pega a posicao dir na string
		nnp = (x+2) + y * (map._ssize[0] +1) #pega a posicao de dir do dir na string
		
		#transforma o mapa em um string linear.
		sMap = list('\n'.join(map._str))
		
		#movimento permitidos... 
		
		if sMap[np] == '0':  #piso
			x += 1
			
		elif sMap[np] == '.': #ponto
			x += 1
			
		elif sMap[np] == '!': #caixa livre
			if sMap[nnp] in ['0','.']: 
				if sMap[nnp] == '0':
					sMap[nnp] = '!'
				elif sMap[nnp] == '.':
					sMap[nnp] = '*'
				
				sMap[np] = '0'
				x += 1
		
		elif sMap[np] == '*': #caixa no ponto
			if sMap[nnp] in ['0','.']: 
				if sMap[nnp] == '0':
					sMap[nnp] = '!'
				elif sMap[nnp] == '.':
					sMap[nnp] = '*'
				
				sMap[np] = '.'
				x += 1
		
		#atualiza as infos no mapa
		s = ''.join(sMap).split('\n')
		self._updateChar(s,(x,y))
		return  map.checkFinalize(),(mapt,(ax,ay))
		
