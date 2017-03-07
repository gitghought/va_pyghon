import re

class UtilStr:

	@classmethod
	def split_N(cls, mlist):
		reg = r'[\n]'
		regS = re.compile(reg)

		new_props = []

		i = 0
		for content in mlist:
			if regS.match(content): 
				continue

			new_props.append(content)

			i+=1
		#print (new_props)

		return new_props

	@classmethod
	def show(cls, mlist) :
		for cont in mlist:
			print (cont)

	#show Dictionary all keys
	@classmethod
	def showDictitonary(cls, mDict) :
		keys = mDict.keys()
		i = 0
		print ("##############################")
		for key in keys :
			print (""+str(i) + " : " + "%-10s" %"" + key.rjust(10, ' '))
			i += 1
		print ("##############################")

if __name__ == "__main__":
	#UtilStr.split_N("")
#	UtilStr.show(["vvv", "vvv"])
	disc = {"a":"a", "b":"b"}
	UtilStr.showDictitonary(disc)

