import io
import sys
import os
import vb_get_dev
import subprocess
import time
import multiprocessing
from vb_get_dev import Dev

class GetProp : 
	def __init__(this, ip):
		this.dev = Dev()
		this.ipaddr = this.dev.connect(ip)
		this.propSav = r".\PropSav.gh"

	def propStrip(this, prop) :
		return prop.strip()

	def propSplit(this, props):
		props = props.split('\n')
		new_props = []
		i = 0
		for prop in props:
			if prop.__len__() == 0:
				continue
			new_props.append(prop)

			i=i+1
		
		return new_props

	def __getPropFromCMD_nothread(this, fileName = "") :
		cmdPreStr = "adb -s "
		cmdStr = cmdPreStr + this.ipaddr + " shell getprop"

		pro = subprocess.Popen(cmdStr, shell = False, stdout = open(this.propSav, 'w'))
		time.sleep(3)
		pro.kill()
		pro.wait()

	def getProp(this, fileName = "") :
		this.__getPropFromCMD_nothread()

	def getPropfromFile(this, fileName) :
		fp = io.open(fileName, 'r')

		try:
			content = fp.read()
			content.strip('\n')
			content.strip()
		finally:
			fp.close()

		return propSplit(content)

	def showFileContent (this, props) :
		for prop in props:
			print (prop)

if __name__ == "__main__" :
	ip = sys.argv[1:]
	if len(ip) == 0:
		print ("bad command : python <command> <ipaddress>")
		exit()

	prop = GetProp(ip)
	prop.getProp("prop.dest")
