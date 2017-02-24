import commands 
import os
import time
import multiprocessing as mp

def getDev():
	headStr = "List of devices attached"
	(status, output) = commands.getstatusoutput("adb devices")
	output = output.strip("\n")
	output = output.strip()
	pos = len(headStr)
	subStr = output[pos:]
	subStr = subStr.strip("\n")
	subStr= subStr.strip()

	if len(subStr)==0:
		return "no devices"
	else:
		res  = subStr.split("\t")
		return res 

def showDev(devs) : 
	for dev in devs:
		print "dev1----->" + dev

def getProp():
	(status,output)=commands.getstatusoutput(adbs + " getprop")
	return output

def connDEV() :
	os.system('adb connect 192.168.1.116')

def stopProcess() :
	global id_logcat

	id_logcat = os.getpid()
	os.system('adb shell logcat > vvv.log')
	time.sleep(1)
	return id


if __name__ == "__main__" :
	#connect device
	#connDEV()

	#
	res = getDev()

	showDev(res)

	#pp = mp.Process(target=stopProcess)
	#print 'before : ', pp, pp.is_alive()

	#pp.start()
	#print 'during : ', pp, pp.is_alive()

	#pp.join(timeout=2)

	#pp.terminate()
	#print 'terminate : ', pp, pp.is_alive()

	#pp.join()
	#print 'join : ', pp, pp.is_alive()
