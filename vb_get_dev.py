import io
import commands 
import os
import multiprocessing
import re
import sys

class Dev:

	# 20170303 ok
	def getDevs(self):
		output = commands.getoutput("adb devices")
		return self.__getIPFromStr(output)

	def __disconnectAll (self) :
		cmdStr = "adb disconnect"
		os.system(cmdStr)


	def connect_nothread (self, ipaddr) :
		cmdStr = "adb connect " + ipaddr[0]
		os.system(cmdStr)

	def connect (self, ipaddr) :
		devs = self.getDevs()
		if len(devs) > 0 :
			self.__disconnectAll()

		if len(ipaddr) == 0:
			print "bad command : python <command> <ipaddress>"
			exit()

		pro = multiprocessing.Process(target=self.connect_nothread, args=(ipaddr,))
		pro.start()
		pro.join(2)
		pro.terminate()
		pro.join()

	def __getIPFromStr(self, ipaddr):
		reg = r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?:[\.\d])(?:[\:])(?:\d{4})'
		s_ip = re.compile(reg, re.M)
		ipList = re.findall(reg,ipaddr)
		#print (ipList)
		return ipList

# just for test
if __name__ == "__main__" :
	dev = Dev()

	ipaddr = sys.argv[1:]

	dev.connect(ipaddr)

	devs = dev.getDevs()
	print (devs)
