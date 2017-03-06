import re
import io
import sys
import os
import vb_get_dev
import subprocess
import time
import multiprocessing
from vb_get_dev import Dev

class GetProp : 
	__need_prop = [
"ro.cantv.homebg",
"ro.cantv.tv.inputcode",
"ro.cantv.app.blacklist",
"ro.build.version.channelid_l",
"ro.umeng.channelid",
"ro.umeng.appkey",
"ro.product.model",
"ro.product.class",
"ro.build.version.channelid",
"ro.product.manufacturer",
"ro.build.version.release",
"ro.build.date.ut"
			]

	def __init__(this, ip  = ""):
		this.dev = Dev()
#		this.ipaddr = this.dev.connect(ip)
		this.ipaddr = this.dev.getDevs()
		this.propSav = r".\PropSav.gh"

	def propStrip(this, prop) :
		return prop.strip()

	def propSplit(this, props):
		props = props.split('\n')
		new_props = []
		i = 0
		for prop in props:
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

	# 

	def __mFilter(this, allContent):
		i = 0
		for content in this.__need_prop :
			if content in allContent:
				return True
		return False

	# return a list
	def myFilter(this, allContent) :
		filt = filter(this.__mFilter, allContent)
		#print (filt)
		#for f in filt :
		#	print ("fff = " + f)

		return filt

	def getPropfromFile(this, fileName = "") :
		reg = r'[\n]'
		regS = re.compile(reg)
		if fileName == "" :
			fp = io.open(this.propSav, 'r')
		else :
			fp = io.open(fileName, 'r')

		new_props = []

		try:
			contents = fp.readlines()
			i = 0
			for content in contents:
				if regS.match(content): 
					continue

				new_props.append(content.strip(r'\n'))

				i+=1
		finally:
			fp.close()

		

		return this.myFilter(new_props)


	# para0 : should be a list
	def showFileContent (this, props) :
		for prop in props:
			print (prop)

if __name__ == "__main__" :
	ip = sys.argv[1:]
	if len(ip) == 0:
		print ("bad command : python <command> <ipaddress>")
		exit()

	prop = GetProp()
	#prop.getProp("prop.dest")
	filt = prop.getPropfromFile()
	prop.showFileContent(filt)

