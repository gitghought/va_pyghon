# -*- coding: utf-8 -*-
import os
import subprocess
import sys
from util_str import UtilStr

class JarInstall :
	projPath = r"F:\mygithub\uiautotest"
	fileName = r"F:\mygithub\uiautotest\bin\uiautotest.jar"
	destPath = r"/sdcard/"
	destFile = r"/sdcard/uiautotest.jar"

	projName = "uiautotest"
	projTargetID = "19"

	dics = {}
	def __init__(this):
		this.dics["createBuild"] = [this.createBuild, "good"]
		this.dics["compile"] = [this.compileFile, this.projPath]
		this.dics["install"] = [this.installJar,[" "r"F:\mygithub\uiautotest\bin\uiautotest.jar", "/sdcard/"]]

		this.dics["execute"] = this.execTest

	# �������ڱ����build.xml
	def createBuild(this, param = []) :
		cmdStr = "android create uitest-project " + " " + " -n " + this.projName + " " + "-t" + " " +this.projTargetID + " " + "-p"  +  " " + this.projPath
		this.__exeInProcessWaitAndNoshell(cmdStr)

	def __exeInProcessWaitAndNoshell(this, cmdStr):
			prop = subprocess.Popen(cmdStr, shell = True, stdout = subprocess.PIPE)
			prop.wait()
			#print (prop.stdout.read())
			return prop

	def __exeInProcessWait(this, cmdStr):
			prop = subprocess.Popen(cmdStr, shell = True, stdout = subprocess.PIPE)
			prop.wait()
			#print (prop.stdout.read())
			return prop

	def compileFile (this, pPath) :
		os.chdir(pPath)

		cmdStr = "ant build"
		prop = subprocess.Popen(cmdStr, shell = True)
		prop.wait()

	def installJar (this,param = []):
		os.chdir(this.projPath)

		cmdStr = "adb push " + param[0] +  " " + param[1]  
		print (cmdStr)
		prop = subprocess.Popen(cmdStr, shell = True)
		prop.wait()

	def execTest (this) :
		cmdStr = "adb shell uiautomator runtest" + " " + this.destFile

		prop = subprocess.Popen(cmdStr, shell = True)
		prop.wait()
		


if __name__ == "__main__":
	ji = JarInstall()
#	ji.compileFile(ji.projPath)
#	ji.installJar(ji.fileName, "/sdcard/")
#	ji.execTest()
	UtilStr.operations(ji.dics)

