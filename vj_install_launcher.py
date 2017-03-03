import multiprocessing
import sys
import os

class InstallLauncher:
	def __installLauncher_nothread(self, filename) :
		cmdStr = "adb push " + filename[1] + " " + filename[0]
		os.system("adb shell rm " + filename[0] + "/" + "OSLauncher*")
		os.system(cmdStr)

	def installLauncher(self, filename):
		pro = multiprocessing.Process(target=self.__installLauncher_nothread(filename))
		pro.start()
		pro.join(5)
		pro.terminate()
		pro.join()

	def isFileExist(self, filename):
		if os.path.isfile(filename):
			return os.path.exists(filename)	


	def __remount_nothread(self):
		cmdStr = "adb shell mount -o rw,remount /system"
		os.system(cmdStr)

	def remount(self):
		pro = multiprocessing.Process(target=self.__remount_nothread())
		pro.start()
		pro.join(2)
		pro.terminate()
		pro.join()


	def __reroot_nothread(self):
		cmdStr = "adb root "
		os.system(cmdStr)

	def reroot(self):
		pro = multiprocessing.Process(target=self.__reroot_nothread())
		pro.start()
		pro.join(2)
		pro.terminate()
		pro.join()


	def __connectDev_noThread(self, ipAddr):
		os.system("adb connect " + ipAddr)

	def connectDev(self, ipAddr):
		pro = multiprocessing.Process(target=self.__connectDev_noThread(ipAddr))
		pro.start()
		pro.join(2)
		pro.terminate()
		pro.join()

if __name__ == "__main__":
	ins = InstallLauncher()	

	commandargs = sys.argv[1:] 
	if len(commandargs) == 0:
		print ("error: python <script> [path] [file]")
		print ("for example : python vvv.py /system/app  OSlauncher.apk")
		exit()

	#print ("" + commandargs[0])
	#print ("" + commandargs[1])
	#args = "".join(commandargs)

	#print (ins.isFileExist(args))


	ipAddr = input("enter ip address :")
	ins.connectDev(ipAddr)

	ins.reroot()

	ins.connectDev(ipAddr)


	ins.remount()

	ins.installLauncher(commandargs)
