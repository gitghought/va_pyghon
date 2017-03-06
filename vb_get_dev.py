#coding=utf-8
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
	devsFile = r".\devs.gh"

	def __isWindows(self):
		return "Window" in platform.system()
	def __isLinux(self):
		return "Linux" in platform.system()

	# return list
	def __getDevsFromFile(self):
		fp = open(self.devsFile, 'r')
		lines = fp.readlines()
		return lines

	def getDevs(self):
		pro = subprocess.Popen("adb devices ", shell = False, stdout = open("devs.gh", 'w'))
		time.sleep(2)
		pro.kill()
		pro.wait()
		devs = self.__getDevsFromFile()

		return devs

	def __disconnectAll (self) :
		cmdStr = "adb disconnect"
		os.system(cmdStr)

	def connect_nothread (self, ipaddr) :
		cmdStr = "adb connect " + ipaddr[0]
		os.system(cmdStr)

	# return string of the ip address include the port
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

# just for test
if __name__ == "__main__" :
	dev = Dev()

	ipaddr = sys.argv[1:]

	ip = dev.connect(ipaddr)
	print ("ip = " + ip)

