import time
import subprocess
from util_str import UtilStr
import sys

class Repo :
	dics = {}
	repoPath = "~/b_h2_allwinner/"
	repoAllwinner = "~/b_h2_allwinner/Allwinner-h2"
	repolichee = "~/b_h2_allwinner/Allwinner-h2"
	def __init__(this):
		this.dics["exit"] = exit
		this.dics["currentBranch"] = this.__repoCurrentBranch
	
	def __repoCurrentBranch(this):
		#cmdStr = "repo forall -c 'git branch -a'"
		#cmdStr = "ls"
		#pro = subprocess.Popen(cmdStr, shell = False)
		#time.sleep(1)
		#pro.kill()
		#pro.wait()
		os.chdir(this.repoPath)
		print (os.curdir)


		return "good"

	def __getPosOfDictionary(this, pos) :
		p = int(pos)
		keys = this.dics.keys()
		i = 0
		for key in keys :
			if i == p:
				return key
			i+=1
	def select(this) :
		pos = 0
		#print (this.dics["pm"]())
		while True:
			UtilStr.showDictitonary(this.dics)
			choice = input("you choice is : ")
			print (this.dics[this.__getPosOfDictionary(choice)]())


if __name__ == "__main__":
	repo = Repo()
	repo.select()
