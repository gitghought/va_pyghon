import sys
from util_str import UtilStr
import subprocess
from vb_get_dev import Dev
import os
import time
import multiprocessing

class SetProp :
	dics = {}

	def __init__(this, ip):
		this.dev = Dev()
		this.dev.connect(ip)

		# 
		this.dics["exit"] = exit
		this.dics["reroot"] = this.__reroot
		this.dics["reboot"] = this.__reboot
		this.dics["debugTrue"] = this.__debugTrue

	def __reboot(this):
		cmdStr = "adb shell reboot"
		pro = subprocess.Popen(cmdStr, shell = False)
		time.sleep(1)
		pro.kill()
		pro.wait()

	def __reroot(this):
		cmdStr = "adb root "

		pro = subprocess.Popen(cmdStr, shell = False)
		time.sleep(1)
		pro.kill()
		pro.wait()

	def __getProp(this, propStrs):
		newCmd=''
		for prop in propStrs:
			newCmd += prop

		return newCmd
	def __listToStr(this, cmdList) :
		newCmd = ""
		for cmd in cmdList:
			newCmd += cmd

		return newCmd

	def __setProp(this, cmdStr):
		print (cmdStr)
		nCmd = this.__listToStr(cmdStr)
		print (nCmd)
		pro = subprocess.Popen(nCmd, shell = False)
		time.sleep(1)
		pro.kill()
		pro.wait()

	def __getPosOfDictionary(this, pos) :
		p = int(pos)
		keys = this.dics.keys()
		i = 0
		for key in keys :
			if i == p:
				return key
			i+=1
	def __debugTrue(this):
		cmdStr = "adb shell setprop persist.sys.log.debug true"

		pro = subprocess.Popen(cmdStr, shell = False)
		time.sleep(1)
		pro.kill()
		pro.wait()

	def setProp(this) :
		pos = 0

		while True:
			UtilStr.showDictitonary(this.dics)
			choice = input("you choice is : ")
			this.dics[this.__getPosOfDictionary(choice)]()

if __name__ == "__main__":
	ipAddr = sys.argv[1:]

	prop = SetProp(ipAddr)
	prop.setProp()
