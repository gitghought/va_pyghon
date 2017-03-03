import subprocess
import time
import os 

class Logcat:

	def getLogcat(self, params=[]):
		cmdStr = "adb shell logcat > aa.log"
		proADB= subprocess.Popen(args = cmdStr, shell=True)

		return proADB



if __name__ == "__main__":
	logcat = Logcat()
	pro = logcat.getLogcat()
	ppid = os.getppid()
	time.sleep(3)

	pro.terminate()
	print ("end")
