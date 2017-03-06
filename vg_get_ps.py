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
	pmFilter = " pm"

	psResultFileName = ".ps.gh"
	psResultList = []

	def __init__(this, ip):
		#this.prop = Prop.Prop()
		this.dev = Dev()
		this.ip = this.dev.connect(ip)

	def __getPsCmd_nothread_danger (this, param = "") :
		cmdPreStr = "adb -s "
		cmdStr = cmdPreStr + this.ip + " shell ps" + " " + param # + " > " + this.psResultFileName
		#os.system(cmdStr)
		pro = subprocess.Popen(cmdStr, shell = False, stdout = open(this.psResultFileName, 'w'))
		time.sleep(2)
		pro.kill()
		pro.wait()


	def __getPsCmdThread(this, param = "") :
		this.__getPsCmd_nothread_danger(param)
		return this.__readFile()

	# return a list
	def __readFile (this) :

		fp = io.open(this.psResultFileName, 'r')

		ncont = []
		try:
			contents = fp.readlines()
			ncont  = UtilStr.split_N(contents)	
			
		finally:
			fp.close()

		return ncont
	def isPmThread(this):
		#reg = ''
		#this.__getPsCmdThread(r' pm')
		#fp = open(this.psResultFileName, 'r')
		#content = fp.read();
		mlist = this.__getPsCmdThread(r'pm')
		if len(mlist) > 0 :
			return True
		else :
			return False


		
		
if __name__ == "__main__":
	ipaddr = sys.argv[1:]

	ps = PsCmd(ipaddr)
	#mlist = ps.__getPsCmdThread()
	#UtilStr.show(mlist)
	print (ps.isPmThread())

