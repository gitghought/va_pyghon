import time
from util_str import UtilStr
import subprocess
import multiprocessing
import sys
import os
from vb_get_dev import Dev

class InstallLauncher:
	#InstallPath

	InstallName = ""
	InstallPath = ""
	dics = {}
	def __init__(this):
		this.dev = Dev()
		launchers = this.__findOldLauncher()
		if len(launchers) > 0:
			this.Launcher = launchers[0]
			this.InstallName = this.__getLauncherInstallName(launchers[0])
			this.InstallPath = this.__getLauncherInstallPath(launchers[0])
		else :
			this.Launcher = "OSLauncher.apk"
			this.InstallName = "OSLauncher.apk"
			this.InstallPath = "/system/priv-app"

		this.dics["installLauncher"] = this.__installLauncher
		this.dics["deleteLauncher"] = this.__delOldLauncher
		this.dics["remount"] = this.__remount
		this.dics["reroot"] = this.__reroot
		this.dics["connect"] = this.__connect
		this.dics["exit"] = exit

	def __installLauncher(this) :
		cmdStr = "adb push "+ this.InstallName.strip('\r \n') + " "  + this.InstallPath
		print (cmdStr)
		pro = subprocess.Popen(cmdStr, shell = False)
		pro.wait()

	def __isFileExist(this, filename):
		if os.path.isfile(filename):
			return os.path.exists(filename)	

	def __reroot(this):
		cmdStr = "adb root"
		pro = subprocess.Popen(cmdStr, shell = False)
		time.sleep(2)
		pro.kill()
		pro.wait()

	def __remount(this):
		cmdStr = "adb shell mount -o rw,remount /system"
		pro = subprocess.Popen(cmdStr, shell = False)
		time.sleep(2)
		pro.kill()
		pro.wait()

	def __reroot(this):
		cmdStr = "adb root "

		pro = subprocess.Popen(cmdStr, shell = False)
		time.sleep(2)
		pro.kill()
		pro.wait()

	def __delOldLauncher(this):
		cmdStr = "adb shell rm \'" + this.Launcher.strip('\r \n') + "\'"
		print (cmdStr)
		
		pro = subprocess.Popen(cmdStr, shell = False)

		time.sleep(2)
		pro.kill()
		pro.wait()

	def __getLauncherInstallName(this, abspath):
		return os.path.split(abspath)[1]

	def __getLauncherInstallPath(this, abspath):
		return os.path.split(abspath)[0]

	# should connect the device first
	def __findOldLauncher(this):
		cmdStr = "adb shell find /system -name OS*.apk"
		pro = subprocess.Popen(cmdStr, shell = False, stdout = subprocess.PIPE)
		pro.wait()
		pathList = pro.stdout.readlines()
		launchers = UtilStr.byteToStr(pathList)
		#print (launchers)
		return launchers

	def launcherOp(this):
		this.__checkPS()

	def __getPosOfDictionary(this, pos) :
		p = int(pos)
		keys = this.dics.keys()
		i = 0
		for key in keys :
			if i == p:
				return key
			i+=1
	def __checkPS(this) :
		pos = 0
		#print (this.dics["pm"]())
		while True:
			UtilStr.showDictitonary(this.dics)
			choice = input("you choice is : ")
			print (this.dics[this.__getPosOfDictionary(choice)]())
	def __connect(this):
		#ipaddr = []
		#ipaddress = input("Enter ip address : ")
		##print (type(ipaddress))
		##print (ipaddress)
		#ipaddr.append(ipaddress)
		this.dev.ops()


if __name__ == "__main__":
	ins = InstallLauncher()	
	ins.launcherOp()
	
