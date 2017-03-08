from util_str import UtilStr
import subprocess
import multiprocessing
import sys
import os

class InstallLauncher:


	def __installLauncher_nothread(this, filename) :
		cmdStr = "adb push " + filename[1] + " " + filename[0]
		os.system("adb shell rm " + filename[0] + "/" + "OSLauncher*")
		os.system(cmdStr)

	def installLauncher(this, filename):
		pro = multiprocessing.Process(target=this.__installLauncher_nothread(filename))
		pro.start()
		pro.join(5)
		pro.terminate()
		pro.join()

	def isFileExist(this, filename):
		if os.path.isfile(filename):
			return os.path.exists(filename)	


	def __remount_nothread(this):
		cmdStr = "adb shell mount -o rw,remount /system"
		os.system(cmdStr)

	def remount(this):
		pro = multiprocessing.Process(target=this.__remount_nothread())
		pro.start()
		pro.join(2)
		pro.terminate()
		pro.join()


	def __reroot_nothread(this):
		cmdStr = "adb root "
		os.system(cmdStr)

	def reroot(this):
		pro = multiprocessing.Process(target=this.__reroot_nothread())
		pro.start()
		pro.join(2)
		pro.terminate()
		pro.join()


	def __connectDev_noThread(this, ipAddr):
		os.system("adb connect " + ipAddr)

	def connectDev(this, ipAddr):
		pro = multiprocessing.Process(target=this.__connectDev_noThread(ipAddr))
		pro.start()
		pro.join(2)
		pro.terminate()
		pro.join()

	# should connect the device first
	def findOldLauncher(this):
		cmdStr = "adb shell find /system -name OS*.apk"
		pro = subprocess.Popen(cmdStr, shell = False, stdout = subprocess.PIPE)
		pro.wait()
		pathList = pro.stdout.readlines()
		launchers = UtilStr.byteToStr(pathList)
		print (launchers)

if __name__ == "__main__":
	ins = InstallLauncher()	
	ins.findOldLauncher()

