import time, os
from colorama import Fore

version = 'v2.9'
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
	print(v+"Type -h or 'help' to show commands\n")


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
	+|     COMMANDS             Name            |+
	+|------------------------------------------|+
	+|   [1] ======> Overload Virus             |+
	+|   [2] ======> Delete All Files Virus     |+
	+|   [3] ======> The Blue Screen Of Death   |+
	+|   [4] ======> You A Fool keyboard        |+
	+|   [5] ======> C,D,E Drive Format         |+
	+|   [6] =====>Shutdown pc unable to turn on|+
	+|   [7] ======> user account flooder       |+
	+|   [8] ======> Delete Os/System           |+
	+|   [9] ======> Endless Notepads           |+
	+|   [10] =====> Bomb Virus                 |+
	+|   [11] =====> Task Kill                  |+
	+|   [12] =====> Net Gone/cut               |+				
	+|   [666] ====> Create All                 |+	
	+|                                          |+		
	+|   [x] ================== About Us        |+
	+|                                          |+
	+|   [0] =================== Exit           |+
	+|                                          |+
 	 ===========================================		
 	""")

	
def aboutus():
	print(f"""
          =============================================
  	  +|             About this tool             |+
  	  =============================================
  	  +|              This Tool Is               |+
          +|               Is Created                |+
    	  +|                   By                    |+
    	  +|            Anikin Luke Abales           |+
     	  +|  for SudoCentercorp team CyberHackers   |+
          +|-----------------------------------------|+
    	  +| Tool name: VirGen | Virus Generator     |+
   	  +| Use To Create computer/mobile virus     |+
    	  +| Tool version: {version}                 |+
          +|-----------------------------------------|+
    	  +|                Contact                  |+
    	  +|             Facebook-Group              |+
    	  +|  facebook.com/groups/sudocyberhackers   |+
          +|                                         |+
     	  +|          Discord invite link            |+
    	  +|     https://discord.gg/H7NXjU9BQ9       |+
          +|--------------^--------^-----------------|+
    	  +| Github: https://github.com/abalesluke   |+
     	  +|                                         |+
    	  +|                 Note!                   |+
          +|   This tool is Originally created by me |+
          +|   so please dont republish it on github |+
          +|   i do not autorized you to edit this   |+
          +|   tool or republish it on github.       |+
          +|                                         |+
          +|         Editing or changing the         |+
          +|       name of the coder or developer    |+
          +|        wont make you a programmer.      |+
          +|                                         |+
          +|        [+]Respect the coder's[+]        |+
          +|     ©️Copyright All Rights Reserved     |+
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


def winerror():
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
	banner2()


