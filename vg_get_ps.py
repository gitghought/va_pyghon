import io
import os
import vd_check_prop as Prop
import vb_get_dev as Dev
import multiprocessing

class PsCmd:
	psResultFileName = ".ps.gh"
	psResultList = []

	def __init__(self) :
		self.prop = Prop.Prop()
		self.dev = Dev.Dev()

	def getPsCmd_nothread_danger (self, param = "") :
		global id_get_ps
		cmdPreStr = "adb -s "

		id_getprop = os.getpid()

		dev = self.dev.connDev()

		cmdStr = cmdPreStr + str(dev) + " shell ps" + " " + param + " > " + self.psResultFileName

		os.system(cmdStr)

	def getPsCmdThread(self, param = "") :


		pro = multiprocessing.Process(target=self.getPsCmd_nothread_danger, args=(param,))
		pro.start()
		pro.join(1)
		pro.terminate()
		pro.join()

	def psSplit(self, psses):
		psses = psses.split('\n')
		new_ps = []
		i = 0
		for ps in psses:
			if ps.__len__() == 0:
				continue
			new_ps.append(ps)

			i=i+1
		
		return new_ps

	def readFile (self) :
		fp = io.open(self.psResultFileName, 'r')

		try:
			content = fp.read()
			content.strip('\n')
			content.strip()
		finally:
			fp.close()

		return self.psSplit(content)
		

#	def psCheckPm(fp) :
			
		
		

if __name__ == "__main__":
	ps = PsCmd()
	ps.getPsCmdThread()
	ps.readFile()
