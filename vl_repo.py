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
		this.dics["localBranch"] = this.__readFileToGetLocalBranch

		this.priv_dics["readFileToGetCurrentBranch"] = this.__readFileToGetCurrentBranch
		this.priv_dics["getAllBranchToFile"] = this.__repoGetAllBranchToFile
	
	def __repoSwitchBranch(this):
		print (os.getcwd())
		print ("oldpath = " + this.oldPath)

	""" read all local branch to list"""
	def __repoLocalBranch(this):
		this.__repoGetAllBranchToFile()
	
		pass

	def __changeToDistPath (this):
		os.chdir(this.repoPath)
		newPath = os.getcwd()

		return newPath

	def __repoGetAllBranchToFile(this):
		this.__changeToDistPath()

		cmdRepo = "repo forall -c "
		cmdGit = "git branch -a"
		cmdStr =  cmdRepo + "\"" + cmdGit + "\""

		pro = subprocess.Popen(cmdStr, shell = True, stdout = open(this.branchFile, 'w'))
		pro.wait()
		
	def __repoCurrentBranch(this):
		# currentpath
		this.oldPath = os.getcwd()

		this.__repoGetAllBranchToFile()

		# get current branch string
		this.curBran = this.__readFileToGetCurrentBranch()

		return this.curBran

	def __readFileToGetCurrentBranch (this):
		fp = open(this.branchFile, 'r')
		str = fp.read()
		# create a reg to filter the current branch
		reg = r'^\*.*'
		starStart = re.compile(reg, re.M)
		ll = starStart.findall(str)
		return ll[0]

	# return local branch into a list
	def __readFileToGetLocalBranch(this):
		# change current path to distenation
		this.__changeToDistPath()
		fp = open(this.branchFile, 'r')
		str = fp.read()
		reg = r'^[ ]{0,}(?!.*remote.*).*'
		starStart = re.compile(reg, re.M)
		ll = starStart.findall(str)

		list1=sorted(set(ll),key=ll.index) 
		UtilStr.show(list1)
		return list1
	
	def select(this) :
		UtilStr.operations(this.dics)

if __name__ == "__main__":
	repo = Repo()
	repo.select()
