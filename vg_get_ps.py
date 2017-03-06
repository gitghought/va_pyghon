from util_str import UtilStr
import sys
import time
import subprocess
import io
import os
#import vd_check_prop as Prop
import vb_get_dev as Dev
import multiprocessing
from vb_get_dev import Dev

class PsCmd:
	psResultFileName = ".ps.gh"
	psResultList = []

	def __init__(self, ip):
		#self.prop = Prop.Prop()
		self.dev = Dev()
		self.ip = self.dev.connect(ip)

	def __getPsCmd_nothread_danger (self, param = "") :
		cmdPreStr = "adb -s "
		cmdStr = cmdPreStr + self.ip + " shell ps" + " " + param # + " > " + self.psResultFileName
		#os.system(cmdStr)
		pro = subprocess.Popen(cmdStr, shell = False, stdout = open(self.psResultFileName, 'w'))
		time.sleep(2)
		pro.kill()
		pro.wait()


	def getPsCmdThread(self, param = "") :
		self.__getPsCmd_nothread_danger(param)
		return self.readFile()
			

	def psSplit(self, psses):
		psses = psses.split('\n')
		new_ps = []
		i = 0
		for ps in psses:
			if ps.__len__() == 0:
				continue
			new_ps.append(ps)

			i=i+1
		
		return new_ps

	def readFile (self) :

		fp = io.open(self.psResultFileName, 'r')

		ncont = []
		try:
			contents = fp.readlines()
			ncont  = UtilStr.split_N(contents)	
			
		finally:
			fp.close()

		return ncont
		
if __name__ == "__main__":
	ipaddr = sys.argv[1:]

	ps = PsCmd(ipaddr)
	mlist = ps.getPsCmdThread()
	UtilStr.show(mlist)
