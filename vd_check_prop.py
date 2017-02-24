import codecs


class Prop:

	propSrc = "prop.src"
	propDest = "prop.dest"

	mListSrc = []
	mListDst = []

	def setMListSrc (self, src):
		self.mListSrc = src

	def setMListDest (self, dest):
		self.mListDst = dest

	def readPropToList(self, srcFile) :
		mList = []

		sFile = codecs.open(srcFile, 'r')
		contents = sFile.read()

		contents.strip('\n')
		contents.strip()
		
		contents = contents.split('\n')

		for content in contents :
			if content.__len__() == 0 :
				continue

			mList.append(content)
	#		print content

		return mList
		
	def isContain (self, propDestName) :
		compRes = []
		#print "isContain->"+ self.propSrc

		#showCentent(mListSrc)

		for self.propSrc in self.mListSrc :
		#	print "isContain->for-->"+propSrc
			ret = propDestName.find(self.propSrc)
			if ret != -1 :
				print propDestName
				
				return 
		

	def compareFileForTrun (propTrun):
		mListSrc = propTrun[0]
		mListDst = propTrun[1]

		showCentent(mListSrc)
		#showCentent(mListDst)

		"""
		showCentent(propTrun[0])
		showCentent(propTrun[1])
		"""

		filter(isContain, mListDst)

	def compareFile (self, propDest):
		#showCentent(propDest)
		filter(self.isContain, propDest)

	def showCentent(self, contents) :
		for content in contents :
			print content

	def readProp(self) :
		mListDst = self.readPropToList(self.propDest)	
		mListSrc = self.readPropToList(self.propSrc)	

		#self.showCentent(mListSrc)
		#self.showCentent(mListDst)

		return (mListSrc, mListDst)


if __name__ == "__main__":
#	mListDst = readPropToList(propDest)	
#	mListSrc = readPropToList(propSrc)	

	prop = Prop()
	print prop.propSrc

	#compareFile(mListDst)
