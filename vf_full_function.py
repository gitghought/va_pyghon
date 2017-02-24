import vb_get_dev as Dev
import vd_check_prop as Prop

class All:

	def __init__(self):
		self.prop = Prop.Prop()
		self.dev = Dev.Dev()

	def connectDevice (self, choice=0):
		self.dev.connect()
		self.dev.connDev(choice)

	def checkProp (self) :
#		self.prop.readProp()
		mListDst = self.prop.readPropToList(self.prop.propDest)	
		mListSrc = self.prop.readPropToList(self.prop.propSrc)	
		self.prop.setMListSrc(mListSrc)
		self.prop.setMListDest(mListDst)
		
		self.prop.compareFile(mListDst)
	

def showList (mList) :
	for val in mList:		
		print val

if __name__ == "__main__":
	all = All()

	#all.connectDevice()
	#all.checkProp()
