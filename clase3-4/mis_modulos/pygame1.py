#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 13:34:04 2018

@author: stevend
"""

import pygame
from pygame import locals

pygame.init()   #inicio de la libreria
pygame.joystick.init()  #inicio del joystick

try:
	j = pygame.joystick.Joystick(0) # create a joystick instance
	j.init() # init instance
	print('Enabled joystick: ',j.get_name())
except pygame.error:
	print('no joystick found.')

while 1:
	for e in pygame.event.get(): # iterate over event stack
		print('event : ' + str(e.type))
		if e.type == pygame.locals.JOYAXISMOTION: # 7
			x, y = j.get_axis(0), j.get_axis(1)
			if round(x)==1: print("he presionado un boton")
			print('x and y : ' + str(x) +' , '+ str(y))
		elif e.type == pygame.locals.JOYBALLMOTION: # 8
			print('ball motion')
		elif e.type == pygame.locals.JOYHATMOTION: # 9
			print('hat motion')
		elif e.type == pygame.locals.JOYBUTTONDOWN: # 10
			print('button down')
		elif e.type == pygame.locals.JOYBUTTONUP: # 11
			print('button up')
 #####