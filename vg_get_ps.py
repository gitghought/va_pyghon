import os
import vd_check_prop as Prop
import vb_get_dev as Dev
import multiprocessing

class PsCmd:

	def __init__(self) :
		self.prop = Prop.Prop()
		self.dev = Dev.Dev()

	def getPsCmd_nothread_danger (self, param = "") :
		global id_get_ps
		cmdPreStr = "adb -s "

		id_getprop = os.getpid()

		dev = self.dev.connDev()

		cmdStr = cmdPreStr + str(dev) + " shell ps" + " " + param

		os.system(cmdStr)

	def getPsCmdThread(self, param = "") :


		pro = multiprocessing.Process(target=self.getPsCmd_nothread_danger, args=(param,))
		pro.start()
		pro.join(1)
		pro.terminate()
		pro.join()

if __name__ == "__main__":
	ps = PsCmd()
	ps.getPsCmdThread()
