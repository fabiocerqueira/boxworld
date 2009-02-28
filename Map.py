# -*- coding: utf-8 -*-
#Copyright (C) 2008 F�bio Cerqueira

import pygame.surface
import pygame.display
import pygame.image
from pygame.locals import HWSURFACE,DOUBLEBUF
from BoxXML import BoxXML
from BoxConst import *


class Map:
	"""Classe responsável por carregar  e desenhar os mapas"""
	def __init__(self,surf):
		self._image = MAPIMAGE 
		
		self._surf = None  #Surface da janela pai
		self._str = None #string que representa o mapa
		self._author = None #string com o nome do autor do mapa
		self._name = None #string com o nome do mapa
		self._ssize = None #tuple(int,int) com a qnt de linhas e colunas do mapa
		self._size = None #tuple(int,int) com a qnt de linhas*30 e colunas*30 do mapa
		self._id = None #int id do mapa
		self._pos = None #list(int,int) posicao do personagem
		
		self._map = None #Surface desenho exib�vel do mapa
		
	
	
	#Inicia as configuracoes do mapa pelo ID
	def setID(self,idMap):
		"""Inicia os atributos do mapa de acordo com o encontrado no XML pelo seu idMap"""
		rMap = BoxXML(MAPSFILE)
		self._id = idMap
		self._author = rMap.getInfoMap(idMap,'author')
		self._name = rMap.getInfoMap(idMap,'name')
		self._str = rMap.getInfoMap(idMap,'str').split()
		self._ssize = tuple(map(int,rMap.getInfoMap(idMap,'size').split(',')))
		self._size = tuple(map(lambda x:30*int(x),rMap.getInfoMap(idMap,'size').split(',')))
		self._surf = pygame.display.set_mode(self._size,HWSURFACE|DOUBLEBUF,32)
		self._pos = list(map(int,rMap.getInfoMap(idMap,'pos').split(',')))
		pygame.display.set_caption(self._name  + ' - by ' + self._author)
			
	
	def _getGraf(self,simbol):
		"""Faz a troca de um elemento de mapa no seu formato string para um elemento gráfico
			retorna uma Surface com a imagem 
		"""
		bpic = pygame.image.load(self._image).convert()
		if simbol != '8':
			simbolos = '@.#!+*0'
			s = simbolos.find(simbol)
			grf = bpic.subsurface((1,1+(30*s)),(30,30))
			return grf	
		else:
			grf = pygame.Surface((30,30),0,32)
			grf.fill((0,0,0))
			return grf
	
		
		
	def draw(self,reDraw = False):
		"""Desenha o mapa
			Para reDraw = True, executa a atualização da imagem com laço somente na linha e coluna que foi modificado.
		"""
		#altera mapa
		if reDraw:
			self._map = self._map.copy()
			px,py = self._pos

			#altera a coluna
			col = zip(*[list(i) for i in self._str])[px]
			for y,c in enumerate(col):
				img = self._getGraf(c)
				self._map.blit(img,(px*30,y*30))

			#altera a linha
			for x,l in enumerate(self._str[py]):
				img = self._getGraf(l)
				self._map.blit(img,(x*30,py*30))
			
		#desenha o mapa
		else:
			self._map = pygame.Surface(self._size,0,32)
			for y,l in enumerate(self._str):
				for x,c in enumerate(l):
					img = self._getGraf(c)
					self._map.blit(img,(x*30,y*30))
		
		#desenha o boneco
		c = 1 if self._str[self._pos[1]][self._pos[0]] == '.' else 0
		self._map.blit(self._getGraf(['@','+'][c]),tuple(map(lambda x:x*30,self._pos))) 
	

				
	def update(self,surf):
		"""Faz o blit na Surface passada em surf e retorna a própria surface
		    screen = obj.update(sreen)
		"""
		surf.blit(self._map,(0,0))
		return surf
				
		
	def checkFinalize(self):
		"""Verifica se o mapa foi finalizado
			True para fim de mapa
		"""
		s = ''.join(self._str)
		return s.find('.') < 0 and s.find('!') < 0
		
	
		
		


