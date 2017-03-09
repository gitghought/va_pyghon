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
	
	repoPath = "/home/gaihao/b_allwinner_h2"
	repoAllwinner = "/home/gaihao/b_allwinner_h2/Allwinner-h2"   
	repolichee = "/home/gaihao/b_allwinner_h2/lichee"   

	def __init__(this):
		this.dics["exit"] = exit
		this.dics["currentBranch"] = this.__repoCurrentBranch
		this.dics["switchBranch"] = this.__repoSwitchBranch
		this.dics["localBranch"] = this.__readFileToGetLocalBranch
		this.dics["updateBranch"] = this.__repoUpdateBranch
		this.dics["remoteBranch"] = this.__readFileToGetRemoteBranch
		this.dics["getAllBranch"] = this.__repoGetAllBranchToFile

		this.priv_dics["readFileToGetCurrentBranch"] = this.__readFileToGetCurrentBranch
		this.priv_dics["getAllBranchToFile"] = this.__repoGetAllBranchToFile
	def __exeInProcessWait(this, cmdStr):
		prop = subprocess.Popen(cmdStr, shell = True)
		prop.wait()

	def __repoUpdateBranch(this):
		cmdStr = "git pull"
		# update Allwinner-h2
		this.__changeToDistPathWithParam(this.repoAllwinner)
		this.__exeInProcessWait(cmdStr)

		# update lichee
		this.__changeToDistPathWithParam(this.repolichee)
		this.__exeInProcessWait(cmdStr)

	def __repoSwitchBranch(this):
		localBranch = this.__readFileToGetLocalBranch()
		UtilStr.show(localBranch)
		choice = input("which branch you want to switch : ")
		branchName = localBranch[int(choice)]
		#print (branchName)
		cmdStr = 'repo forall -c git co ' + branchName 
		#print (cmdStr)
		pro = subprocess.Popen(cmdStr, shell = True)
		pro.wait()


	""" read all local branch to list"""
	def __repoLocalBranch(this):
		this.__repoGetAllBranchToFile()
	
		pass

	def __changeToDistPathWithParam (this, path) :
		os.chdir(path)
		newPath = os.getcwd()

		return newPath
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
		#print(this.curBran)
		UtilStr.show(this.curBran)

		return this.curBran

	def __readFileToGetCurrentBranch (this):
		fp = open(this.branchFile, 'r')
		str = fp.read()
		# create a reg to filter the current branch
		reg = r'^\*.*'
		starStart = re.compile(reg, re.M)
		ll = starStart.findall(str)
		#list1=sorted(set(ll),key=ll.index) 
		return this.__removeRepeated(ll)

	# return remote branch into a list
	def __readFileToGetRemoteBranch(this) :
		# change current path to distenation
		this.__changeToDistPath()
		fp = open(this.branchFile, 'r')
		str = fp.read()
		reg = r'^[ ]{0,}.*remote.*'
		starStart = re.compile(reg, re.M)
		ll = starStart.findall(str)

		return this.__removeRepeated(ll)

	# return local branch into a list
	def __readFileToGetLocalBranch(this):
		# change current path to distenation
		this.__changeToDistPath()
		fp = open(this.branchFile, 'r')
		str = fp.read()
		reg = r'^[ ]{0,}(?!.*remote.*).*'
		starStart = re.compile(reg, re.M)
		ll = starStart.findall(str)

		return this.__removeRepeated(ll)

	def __removeRepeated(this, oldList):
		list1=sorted(set(oldList),key=oldList.index) 
		UtilStr.show(list1)
		return list1
	
	def select(this) :
		UtilStr.operations(this.dics)

if __name__ == "__main__":
	repo = Repo()
	repo.select()
