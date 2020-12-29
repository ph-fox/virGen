import os, time
from .banner import *

def windows():
	while True:
		banner2()
		print("Type -h to show commands\n")
		ui = input(g+"win > ")
		if(ui == '1'):
			print("Nice")
		elif(ui == '2'):
			return()
		