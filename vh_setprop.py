import os
import multiprocessing

class SetProp :
	def reroot_nothread(self):
		cmdStr = "adb root "
		os.system(cmdStr)

	def reroot(self):
		pro = multiprocessing.Process(target=self.reroot_nothread)
		pro.start()
		pro.join(2)
		pro.terminate()
		pro.join()

	def getProp(self, propStrs):
		newCmd=''
		for prop in propStrs:
			newCmd += prop

		return newCmd

	def setProp(self, propStr):
		cmdStr = "adb shell setprop "
		os.system(cmdStr + propStr)

	def checkProp(self, propStr):
		cmdStr = "adb shell getprop | grep "
		os.system(cmdStr + propStr)
	
	def enableSet():
		cmdStr = "adb shell reboot"

	def connectDev_noThread(self, ipAddr):
		os.system("adb connect " + ipAddr)

	def connectDev(self, ipAddr):
		pro = multiprocessing.Process(target=connectDev_noThread, args=(ipAddr,))
		pro.start()
		pro.join(2)
		pro.terminate()
		pro.join()
		


if __name__ == "__main__":
	prop = SetProp()

	ipAddr = input("enter ip address :")
	prop.connectDev_noThread(ipAddr)

	prop.reroot()

	os.system("adb connect " + ipAddr)

	propStr = prop.getProp("persist.sys.log.debug true")
	prop.setProp(propStr)
	prop.checkProp("persist.sys.log.debug")

