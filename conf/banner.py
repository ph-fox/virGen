import time, os
from colorama import Fore

#color section
f = Fore
v = f.MAGENTA
r = f.RED
g = f.GREEN
y = f.YELLOW
c = f.CYAN
b = f.BLUE


def banner1():

	print(r+"""

╦  ╦┬┬─┐╔═╗┌─┐┌┐┌
╚╗╔╝│├┬┘║ ╦├┤ │││
 ╚╝ ┴┴└─╚═╝└─┘┘└┘

   Virus|Generator
	""")
	print(y+"By: Anikin Luke\n")


def banner2():

	print(c+"""

╦ ╦  ╦  ╔╗╔  ╔╦╗  ╔═╗  ╦ ╦  ╔═╗
║║║  ║  ║║║   ║║  ║ ║  ║║║  ╚═╗
╚╩╝  ╩  ╝╚╝  ═╩╝  ╚═╝  ╚╩╝  ╚═╝

	Windows Virus
		""")
	print(y+"By: Anikin Luke\n")



def banner3():

	print(c+"""

╦    ╦  ╔╗╔  ╦ ╦  ═╗ ╦
║    ║  ║║║  ║ ║  ╔╩╦╝
╩═╝  ╩  ╝╚╝  ╚═╝  ╩ ╚═

	Linux virus
		""")
	print(y+"By: Anikin Luke\n")


def banner4():

	print(c+"""

╔═╗  ╔╗╔  ╔╦╗  ╦═╗  ╔═╗  ╦  ╔╦╗
╠═╣  ║║║   ║║  ╠╦╝  ║ ║  ║   ║║
╩ ╩  ╝╚╝  ═╩╝  ╩╚═  ╚═╝  ╩  ═╩╝
	
	Android Virus
		""")
	print(y+"By: Anikin Luke\n")


def banner5():

	print(c+"""

╦  ╔═╗  ╔═╗
║  ║ ║  ╚═╗
╩  ╚═╝  ╚═╝		
	
	IOS Virus
		""")
	print(y+"By: Anikin Luke\n")


def help():
		print("""  
	==============================================
	+|VirGen VirusGenerator coded By:Anikin Luke|+
	==============================================
	+|     COMMANDS            Decription       |+
	+|------------------------------------------|+
	+|   [1] =======   Windows virus generator  |+
	+|   [2] ==========  Linux Virus Generator  |+
	+|   [3] ========= Android virus Generator  |+
	+|   [4] ============= IOS virus Generator  |+
	+|   [5] ================== About Us        |+
	+|                                          |+
	+|   [0] =================== Exit           |+
	+|                                          |+
 	 ===========================================		
 	""")


def winhelp():
	print("""  
	==============================================
	+|VirGen VirusGenerator coded By:Anikin Luke|+
	==============================================
	+|     COMMANDS            Decription       |+
	+|------------------------------------------|+
	+|   [1] =======   	 Overload Virus         |+
	+|   [2] =======	 			            |+
	+|   [3] =======			                |+
	+|   [4] =======  						    |+
	+|   [5] ================== About Us        |+
	+|                                          |+
	+|   [0] =================== Exit           |+
	+|                                          |+
 	 ===========================================		
 	""")




def error():
	time.sleep(2)
	os.system("clear")
	print("\n\nE")
	time.sleep(.1)
	os.system("clear")
	print("\n\nEr")
	time.sleep(.1)
	os.system("clear")
	print("\n\nErr")		
	time.sleep(.1)
	os.system("clear")
	print("\n\nErro")		
	time.sleep(.1)
	os.system("clear")
	print("\n\nError!")
	time.sleep(.1)
	os.system("clear")
	banner1()


