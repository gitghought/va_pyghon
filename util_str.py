import re

class UtilStr:

	@classmethod
	def byteToStr (cls, mlist):
		ll = []
		for l in mlist:
			ll.append(l.decode(encoding = 'utf-8'))

		return ll

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

	@classmethod
	def operations(cls, dics):
		cls.__ops(dics)

	@classmethod
	def __getPosOfDictionary(cls, dics, pos) :
		p = int(pos)
		keys = dics.keys()
		i = 0
		for key in keys :
			if i == p:
				return key
			i+=1

	@classmethod
	def __ops(cls,dics) :
		pos = 0
		#print (this.dics["pm"]())
		cls.flag = 0
		while True:
			if cls.flag :
				break
			UtilStr.showDictitonary(dics)
			choice = input("you choice is : ")
			print (dics[cls.__getPosOfDictionary(dics, choice)]())

if __name__ == "__main__":
	#UtilStr.split_N("")
#	UtilStr.show(["vvv", "vvv"])
	dics = {"a":"a", "b":"b"}
	#UtilStr.showDictitonary(disc)
	UtilStr.operations(dics)

