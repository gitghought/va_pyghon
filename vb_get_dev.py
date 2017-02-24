
import commands 
import os

def devSplit(dev) :
	newDev=dev.split('\t')	
	newDev.pop(1)

	return str(newDev)

def devsSplit(devs):
	devs = devs.split('\n')
	new_devs = []
	i = 0
	for dev in devs:
		new_devs.append(devSplit(dev))
		i=i+1
	
	return new_devs

def getDevs():
	headStr = "List of devices attached"
	(status, output) = commands.getstatusoutput("adb devices")
	output = output.strip("\n")
	output = output.strip()
	pos = len(headStr)
	subStr = output[pos:]
	subStr= subStr.strip()
	subStr = subStr.strip("\n")

	if len(subStr)==0:
		return "no devices"
	else:
		return devsSplit(subStr)

def showDevs(devs) : 
	i = 0
	for dev in devs:
		print "dev["+ str(i) +"]----->" + dev
		i=i+1
def selectDevFromDevs(devs): 
	if devs.__len__() >= 2:
		val = input("you choice")
		print val
	else:
		return 0
	

if __name__ == "__main__" :
	#connect device
	#connDEV()

	#
	res = getDevs()
	print res.__len__()
	showDevs(res)
	choice = selectDevFromDevs(res)
	

