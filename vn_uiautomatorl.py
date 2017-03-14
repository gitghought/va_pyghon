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
	
	testDics = {}

	# 说明： 字典中存储的是列表，列表第一个元素是待调用的方法，第二个元素仍然是列表，分别存储路径、文件名和参数
	# 说明：具体格式还需要参考实际使用的命令要求的格式进行填写
	dics = {}
	
	@classmethod
	def __getPosOfDictionary(this, dics, pos) :
		p = int(pos)
		keys = dics.keys()
		i = 0
		for key in keys :
			if i == p:
				return key
			i+=1


	def __init__(this):
		this.dics["createBuild"] = [this.createBuild, []]
		this.dics["compile"] = [this.compileFile, [r"F:\mygithub\uiautotest", ]]
		this.dics["install"] = [this.installJar,[r"F:\mygithub\uiautotest\bin\uiautotest.jar", "/mnt/shell/emulated/"]]
		this.dics["execute"] = [this.execTest, []]
		this.dics["executePackage"] = [this.execTestPackage, ["/mnt/shell/emulated/uiautotest.jar", "com.simple.UIAutoTestLauncher"]]
		this.dics["executePackageCanApp"] = [this.execTestPackage, ["/mnt/shell/emulated/uiautotest.jar", "com.simple.UIAutoTestCanApp"]]
		this.dics["executePackageCanAppMethod"] = [this.execTestPackage, ["/mnt/shell/emulated/uiautotest.jar", "com.simple.UIAutoTestCanApp", "#"]]
		#this.dics["executePackageMethod"] = [this.execTestPackage, ["/mnt/shell/emulated/UiAutotestLauncher.jar",]]
		
		this.testDics["推荐位"] = ["testOptionSuggest"]
		this.testDics["获取所有子组件"] = ["testGetAllChildObject"]
		
	# �������ڱ����build.xml
	def createBuild(this, param = []) :
		cmdStr = "android create uitest-project " + " " + " -n " + this.projName + " " + "-t" + " " +this.projTargetID + " " + "-p"  +  " " + this.projPath
		this.__exeInProcessWaitAndNoshell(cmdStr)

	def __exeInProcessWaitAndNoshell(this, cmdStr):
			prop = subprocess.Popen(cmdStr, shell = True, stdout = subprocess.PIPE)
			prop.wait()
			return prop

	def __exeInProcessWait(this, cmdStr):
			prop = subprocess.Popen(cmdStr, shell = True, stdout = subprocess.PIPE)
			prop.wait()

			return prop

	def compileFile (this, params = []) :
		os.chdir(params[0])

		cmdStr = "ant build"
		prop = subprocess.Popen(cmdStr, shell = True)
		prop.wait()

	def installJar (this,param = []):
		os.chdir(this.projPath)

		cmdStr = "adb push " + param[0] +  " " + param[1]  
		print (cmdStr)
		prop = subprocess.Popen(cmdStr, shell = True)
		prop.wait()

	def execTest (this, params = []) :
		cmdStr = "adb shell uiautomator runtest" + " " + params[0]

		prop = subprocess.Popen(cmdStr, shell = True)
		prop.wait()
	def execTestPackage (this, params = []):
		if len(params) == 3 :
			UtilStr.showDictitonary(this.testDics)
			choice = input ("which method you want to execute : ")
			keyStr = this.__getPosOfDictionary(this.testDics, choice)
			print (keyStr)
			cmdStr = "adb shell uiautomator runtest" + " " + params[0] + " " +  " -c " + params[1] + params[2] + this.testDics[keyStr][0]
			print (cmdStr)
		else :
			cmdStr = "adb shell uiautomator runtest" + " " + params[0] + " " +  " -c " + params[1]
			print (cmdStr)

		prop = subprocess.Popen(cmdStr, shell = True)
		prop.wait()
		
if __name__ == "__main__":
	ji = JarInstall()
	UtilStr.operations(ji.dics)

