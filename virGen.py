import os, time
from conf.banner import *
from conf.windows import *
print("Grant us root password by Entering it below.\nwe need root access to install some requirements")
os.system("sudo apt-get install python3-pip")
os.system("sudo pip3 install colorama")
os.system("clear")
from colorama import Fore
banner1()

while True:
	ui = input(g+"AL104~: ").lower()
	if(ui == "help" or ui == "-h"):
		help()
	
	elif(ui == '1'):
		windows()

	elif(ui == '2'):
		print('Comming Soon!')

	elif(ui == '3'):
		print("Comming Soon!")

	elif(ui == '4'):
		print('Comming Soon!')

	elif(ui == '0'):
		print("Bye..😥️")
		os.system("clear")
		break

	else:
		print("Error! command not found!\nTry executing -h\n")
		error()
		
