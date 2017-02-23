import commands 

adbs="adb shell"

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

def getProp():
	(status,output)=commands.getstatusoutput(adbs + " getprop")
	return output

print "" + getProp()
