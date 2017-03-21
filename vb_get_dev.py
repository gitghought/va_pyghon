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
	def __init__(this):
		this.dics["connect"] = this.__connect
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

                print (devs)

		return devs

	def __disconnectAll (self) :
		cmdStr = "adb disconnect"
		os.system(cmdStr)

	def connect_nothread (self, ipaddr) :
		cmdStr = "adb connect " + ipaddr[0]
		os.system(cmdStr)

	def __connect(this) :
		ipaddr = []

		ipaddress = raw_input("enter ip address : ")
		ipaddr.append(ipaddress)
		this.connect(ipaddr)

	# return string of the ip address include the port
	# param1:should be a list
	def connect (self, ipaddr) :
		devs = self.getDevs()
		if len(devs) > 0 :
			self.__disconnectAll()

		if len(ipaddr) == 0:
			print ("bad command : python <command> <ipaddress>")
			exit()

		pro = multiprocessing.Process(target=self.connect_nothread, args=(ipaddr,))
		pro.start()
		pro.join(2)
		pro.terminate()
		pro.join()

		devs = self.getDevs()
		#print ("defs = " + self.__getIPFromStr(str(devs))[0])

		return self.__getIPFromStr(str(devs))[0]


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

