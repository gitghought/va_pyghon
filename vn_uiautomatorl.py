import os
import subprocess
import sys

class JarInstall :
	projPath = r"D:\vv_uiautotest\uiautotest"
	fileName = r"D:\vv_uiautotest\uiautotest\bin\uiautotest.jar"
	destPath = r"/sdcard/"
	destFile = r"/sdcard/uiautotest.jar"

	dics = {}
	def __init__(this):
		this.dics["build"] = this.compileFile
	
	def createBuild(this) :
		pass

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

