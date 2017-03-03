import io
import os
import vb_get_dev
import multiprocessing
from vb_get_dev import Dev

class GetProp : 
	def __init__(this):
		this.dev = Dev()

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

	def __getPropFromCMD_nothread(this, fileName) :

		global id_getprop
		cmdPreStr = "adb -s "

		id_getprop = os.getpid()

		dev = this.dev.getDev()
		cmdStr = cmdPreStr + dev[0] + " shell getprop  > " + fileName

		print cmdStr 

		os.system(cmdStr)

	def getProp(this, fileName) :
		pro = multiprocessing.Process(target=this.__getPropFromCMD_nothread, args=(fileName,))
		pro.start()
		pro.join(2)
		pro.terminate()
		pro.join()


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
			print prop

if __name__ == "__main__" :
	prop = GetProp()
	prop.getProp("prop.dest")
