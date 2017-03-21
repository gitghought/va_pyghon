#coding=utf-8

from util_str import UtilStr
import platform
import os.path
import time
import subprocess
import multiprocessing
import io
import os
import re
import sys

class Dev:
	devsFile = r"devs.gh"

	dics = {}
	dicsUI = {}
	def __init__(this):

		this.dicsUI["connect"] = this.ghconnect
		this.dicsUI["disconnect"] = this.disconnect
		this.dicsUI["back"] = this.__back

		this.dics["connect"] = this.__connect
		this.dics["disconnect"] = this.__disconnectAll
		this.dics["back"] = this.__back

	def __isWindows(self):
		return "Window" in platform.system()
	def __isLinux(self):
		return "Linux" in platform.system()

	def __back(this) :
		UtilStr.flag = 1

	# return list
	def __getDevsFromFile(self):
		fp = open(self.devsFile, 'r')
		lines = fp.readlines()
		return lines

	def getDevs(self):
		pro = subprocess.Popen("adb devices ", shell = True, stdout = open("devs.gh", 'w'))
		time.sleep(2)
		pro.kill()
		pro.wait()
		devs = self.__getDevsFromFile()

# 		print (devs)

		return devs
	
	def disconnect(self):
		self.__disconnectAll()

	def __disconnectAll (self) :
		cmdStr = "adb disconnect"
		os.system(cmdStr)

	def  ghconnect(self, ipaddrstr) :
		cmdStr = "adb connect " + ipaddrstr

		devs = self.getDevs()
		if len(devs) > 0 :
			self.__disconnectAll()

# 		pro = multiprocessing.Process(target=self.connect_nothread, args=(ipaddr,))
 		pro = subprocess.Popen(cmdStr, shell = True)
 		time.sleep(10)
 		pro.kill()
 		pro.wait()

		devs = self.getDevs()
		print (str(devs))
		if len(devs) == 0 :
			print (len(devs))
			return ""

		ret  = self.__getIPFromStr(str(devs))
# 		print (len(ret))
		if len(ret) == 0:
			return ""
		else :
			return ret[0]

	def __connect(this) :
		ipaddr = []

		ipaddress = raw_input("enter ip address : ")
		ipaddr.append(ipaddress)
		this.connect(ipaddr)

	# return string of the ip address include the port
	# param1:should be a list
	def connect (self, ipaddr) :
		cmdStr = "adb connect " + ipaddr[0]

		devs = self.getDevs()
		if len(devs) > 0 :
			self.__disconnectAll()

		if len(ipaddr) == 0:
			print ("bad command : python <command> <ipaddress>")
			exit()

# 		pro = multiprocessing.Process(target=self.connect_nothread, args=(ipaddr,))
 		pro = subprocess.Popen(cmdStr, shell = True)
 		pro.wait()

		devs = self.getDevs()
		print (str(devs))
		if len(devs) == 0 :
			print (len(devs))
			return ""

		ret  = self.__getIPFromStr(str(devs))
# 		print (len(ret))
		if len(ret) == 0:
			return ""
		else :
			return ret[0]

	# para0:should be string
	def __getIPFromStr(self, ipaddr):
		reg = r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?:[\.\d])(?:[\:])(?:\d{4})'
		s_ip = re.compile(reg, re.M)
		ipList = re.findall(reg,ipaddr)
		return ipList

	def ops(this):
		UtilStr.operations(this.dics)


# just for test
if __name__ == "__main__" :
#	print(os.path.abspath("."))
 	dev = Dev()
 	dev.ops()

