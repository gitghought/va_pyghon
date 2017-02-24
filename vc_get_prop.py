import io
import os
import vb_get_dev
import multiprocessing

def propStrip(prop) :
	return prop.strip()

def propSplit(props):
	props = props.split('\n')
	new_props = []
	i = 0
	for prop in props:
		if prop.__len__() == 0:
			continue
		new_props.append(prop)

		i=i+1
	
	return new_props

def getPropFromCMD_nothread(fileName) :

	global id_getprop
	cmdPreStr = "adb -s "

	id_getprop = os.getpid()

	dev = vb_get_dev.connDev()
	cmdStr = cmdPreStr + str(dev) + " shell getprop  > " + fileName

	print cmdStr 

	os.system(cmdStr)

def getPropFromCMDThread(fileName) :
	pro = multiprocessing.Process(target=getPropFromCMD_nothread, args=(fileName,))
	pro.start()
	pro.join(2)
	pro.terminate()
	pro.join()


def getPropfromFile(fileName) :
	fp = io.open(fileName, 'r')

	try:
		content = fp.read()
		content.strip('\n')
		content.strip()
	finally:
		fp.close()

	return propSplit(content)

def showFileContent (props) :
	for prop in props:
		print prop

if __name__ == "__main__" :
	getPropFromCMDThread("prop.dest")
