import re
import os
import time
import subprocess
from util_str import UtilStr
import sys

class Repo :
	dics = {}
	priv_dics = {}
	
	branchFile = "branch.gh"
	
	repoPath = "/home/gaihao/b_h2_allwinner/"
	repoAllwinner = "/home/gaihao/b_h2_allwinner/Allwinner-h2"
	repolichee = "/home/gaihao/b_h2_allwinner/Allwinner-h2"
	def __init__(this):
		this.dics["exit"] = exit
		this.dics["currentBranch"] = this.__repoCurrentBranch
		this.dics["switchBranch"] = this.__repoSwitchBranch

		this.priv_dics["readfile"] = this.__readFile
	
	def __repoSwitchBranch(this):
		print (os.getcwd())
		print ("oldpath = " + this.oldPath)
		
	def __repoCurrentBranch(this):
		# currentpath
		this.oldPath = os.getcwd()

		# distpath
		os.chdir(this.repoPath)
		newPath = os.getcwd()

		cmdRepo = "repo forall -c "
		cmdGit = "git branch -a"
		cmdStr =  cmdRepo + "\"" + cmdGit + "\""

		pro = subprocess.Popen(cmdStr, shell = True, stdout = open(this.branchFile, 'w'))
		pro.wait()

		# get current branch string
		curBran = this.__readFileToGetCurrentBranch()

		return curBran

	def __readFileToGetCurrentBranch (this):
		fp = open(this.branchFile, 'r')
		str = fp.read()
		#print (str)
		# create a reg to filter the current branch
		reg = r'^\*.*'
		starStart = re.compile(reg, re.M)
		ll = starStart.findall(str)
		return ll[0]
	
	def select(this) :
		UtilStr.operations(this.dics)

if __name__ == "__main__":
	repo = Repo()
	repo.select()
