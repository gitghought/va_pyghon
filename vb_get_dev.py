import io
import commands 
import os
import multiprocessing

class Dev:

	devIP = ("192.168.1.116", "192.168.155.5")

	def devSplit(self, dev) :
		newDev=dev.split('\t')	
		newDev.pop(1)

		return str(newDev)

	def devsSplit(self, devs):
		devs = devs.split('\n')
		new_devs = []
		i = 0
		for dev in devs:
			new_devs.append(self.devSplit(dev))
			i=i+1
		
		return new_devs

	# haven't done yet
	def confDev (self, fileName) :
		io.open(fileName,'r')
		print res

	def getDevs(self):
		headStr = "List of devices attached"

		print ("begin dev->getDevs")

		(status, output) = commands.getstatusoutput("adb devices")
		output = output.strip("\n")
		output = output.strip()
		pos = len(headStr)
		subStr = output[pos:]
		subStr= subStr.strip()
		subStr = subStr.strip("\n")

		print ("before dev->getDevs")

		if len(subStr)==0:
			return "no devices"
		else:
			return self.devsSplit(subStr)

	def showDevs(self, devs) : 
		i = 0
		for dev in devs:
			print "dev["+ str(i) +"]----->" + dev
			i=i+1

	def selectDevFromDevs(self, devs): 
		if devs.__len__() >= 2:
			val = input("you choice")
			return val
		else:
			return 0

	def __disconnectAll (self) :
		cmdStr = "adb disconnect"
		os.system(cmdStr)

	def connect_nothread(self, ip) :
		global id_connectIP
		cmdPreStr = "adb -s "
		id_connectIP = os.getpid()
		os.system("adb connect" + " " + ip)

	# don't use no thread 
	def connect (self) :
		self.__disconnectAll()

		i = 0
		for ip in self.devIP :
			pro = multiprocessing.Process(target=self.connect_nothread, args=(ip,))
			pro.start()
			pro.join(2)
			pro.terminate()
			pro.join()
		
	# return exectly ip 
	def connDev(self, choice = 0) :
		connStr = "adb -s "

		print ("begin connDev")

		devs = self.getDevs()
		self.showDevs(devs)
		#choice = selectDevFromDevs(devs)
	#:	print "choice = " + str(choice)
		return devs[choice].lstrip('[').rstrip(']').lstrip('\'').rstrip('\'')
		

# just for test
if __name__ == "__main__" :
	#connect device
	#connDEV()

	# test getdev
	#res = getDevs()
	#print res.__len__()
	#showDevs(res)
	#choice = selectDevFromDevs(res)
	

#	confDev("devicelist.in")
	dev = connDev()
	print type(dev)

