#!/usr/bin/python
# Author: Azaharuddin
import shutil
from os import system, path, chdir, getcwd, popen
from json import loads

# Definitions Goes here
class FixPatch:
    def __init__(self):
	maindir=getcwd()
	patchdir="/device/xiaomi/msm8956-common/patch/"
	chdir(maindir)
	chdir("frameworks/av")
	cmd="git am {}".format(maindir + patchdir + "0001-fix-Miracast-for-devices-using-HDCP-method.patch")
	response=system(cmd)
	if response==0:
		mirap=1
	elif response==32768:
		system("git am --abort")
	chdir(maindir)
	chdir("system/bt")
	cmd="git am {}".format(maindir + patchdir + "0001-Revert-Add-support-to-force-disable-enhanced-sco-com.patch")
	response=system(cmd)
	if response==32768:
		system("git am --abort")
		btp=0
	elif response==0:
		btp=1
	if btp==1:
		cmd="git am {}".format(maindir + patchdir + "0002-Add-support-force-disable-sco-enhanced-sync-commands.patch")
		response=system(cmd)
		if response==32768:
			system("git am --abort")
			system("git reset --hard HEAD~1")
		elif response==0:
			btp=2
	chdir(maindir)
# Main Prog
if __name__=="__main__":
    FixPatch()
