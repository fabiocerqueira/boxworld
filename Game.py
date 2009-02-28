# -*- coding: utf-8 -*-
#Copyright (C) 2008 Fábio Cerqueira

import pygame.event
import pygame.display
from pygame.locals import NOFRAME
from pygame import QUIT,KEYDOWN,K_UP,K_DOWN,K_LEFT,K_RIGHT,K_w,K_r,K_z,KMOD_CTRL
from Map import Map
from Character import Character
from sys import exit
from os import environ

environ['SDL_VIDEO_CENTERED'] = '1'

class Game:
	"""Classe que representa o jogo"""
	def __init__(self):
		self.pilha = [] #pilha usada para o desfazer
		self.win = False #True caso tenha finalizado o mapa
		self.fase = 0 #id do mapa que está em jogo
		self.screen = None #Tela principal do jogo
		self.map = None #Map em jogo
		self.person = None #Personagem
			
	def init(self):
		"""MÃ©todo para iniciar o jogo completo"""
		#inicia a janela 'invisível'
		self.screen = pygame.display.set_mode((1,1),NOFRAME,32)
		
		
		#cria uma instancia para o mapa
		self.map = Map(self.screen)
		pygame.display.set_icon(self.map._getGraf('!'))
		#cria personagem 
		self.person = Character(self.map,self.screen)

		#incia mapa self.fase
		self.mapInit()
		
		#Comeca o jogo
		self.screen = self.update()
		
		
		#laço principal do jogo
		while True:		
			for event in pygame.event.get():
				if event.type == QUIT:
					self.exit()
				if event.type == KEYDOWN:
					
					#movimentos do personagem
					if event.key == K_UP: #cima
						self.win,s = self.person.up()
						self.pushPilha(s)
					elif event.key == K_DOWN: #baixo
						self.win,s = self.person.down()
						self.pushPilha(s)
					elif event.key == K_LEFT: #esquerda
						self.win,s = self.person.left()
						self.pushPilha(s)
					elif event.key == K_RIGHT: #direita
						self.win,s = self.person.right()
						self.pushPilha(s)
						
					elif event.key == K_w: #ganha
						self.win = True
					elif event.key == K_r: #reincia o mapa
						self.mapInit()
						self.screen = self.update()
						
					elif event.key == K_z and pygame.key.get_mods() & KMOD_CTRL: #ctrl + z
						self.desfazer()
						self.screen = self.update()
				
			pygame.display.flip()
			if self.win:
				self.fase = (self.fase+1) % 16
				self.mapInit()
				self.screen = self.update()
	#end init
	
	
	def pushPilha(self,s):
		"""MÃ©todo adiciona o Ãºltimo estado do jogo a pilha do desfazer. Adiciona no mÃ¡ximo 5 estados.
			obj.pushPilha(estado)
			estado ->  (['mapa'],(x,y))
		"""
		if len(self.pilha) > 5:
			del self.pilha[0]
		self.pilha.append(s)
		
	def popPilha(self):
		"""MÃ©todo pop do desfazer"""
		if len(self.pilha) > 0:
			return self.pilha.pop()
		return None
		
	def desfazer(self):
		"""Recupera os estados salvos na pilha para desfazer o jogo"""
		ns = self.popPilha()
		if ns:
			self.map._str = ns[0]
			self.map._pos = ns[1]
			self.map.draw()
			
		
	def mapInit(self):
		"""Inicia um mapa"""
		#Marca estado com não vitorioso
		self.win = False
		#zera a pilha do desfazer
		self.pilha = []
		#define o mapa de inicio
		self.map.setID(self.fase)
		#desenha o mapa
		self.map.draw()
		
	
	def update(self):
		"""Atualiza jogo"""
		return self.person.update()
		
	def exit(self):
		"""Sai do jogo"""
		exit()
		
