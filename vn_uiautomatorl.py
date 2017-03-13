# -*- coding: utf-8 -*-
import os
import subprocess
import sys

class JarInstall :
	projPath = r"F:\mygithub\uiautotest"
	fileName = r"F:\mygithub\uiautotest\bin\uiautotest.jar"
	destPath = r"/sdcard/"
	destFile = r"/sdcard/uiautotest.jar"

	projName = "uiautotest"
	projTargetID = "19"

	dics = {}
	def __init__(this):
		this.dics["createBuild"] = this.createBuild
		this.dics["build"] = this.compileFile
		this.dics["install"] = this.installJar
		this.dics["execute"] = this.execTest

	# 创建用于编译的build.xml
	def createBuild(this) :
		#android create uitest-project -n uiautotest -t 19 -p F:\mygithub\uiautotest
		cmdStr = "android create uitest-project " + " " + " -n " + this.projName + "" + "-t" + this.projTargetID + " " + "-p"  + this.projPath
		print (cmdStr)


	def compileFile (this, pPath) :
		os.chdir(pPath)

		cmdStr = "ant build"
		prop = subprocess.Popen(cmdStr, shell = True)
		prop.wait()

	def installJar (this, fileName, distPath) : 
		os.chdir(this.projPath)

		cmdStr = "adb push " + fileName +  " " + distPath  
		print (cmdStr)
		prop = subprocess.Popen(cmdStr, shell = True)
		prop.wait()

	def execTest (this) :
		cmdStr = "adb shell uiautomator runtest" + " " + this.destFile

		prop = subprocess.Popen(cmdStr, shell = True)
		prop.wait()
		


if __name__ == "__main__":
	ji = JarInstall()
	ji.compileFile(ji.projPath)
	ji.installJar(ji.fileName, "/sdcard/")
	ji.execTest()

