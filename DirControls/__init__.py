from os import path
import LanguageControls
import os

CURRENT_EXECUTABLES = []
PATH_EXECUTABLES = []

#https://stackoverflow.com/questions/63234890/python3-shorten-path-for-home-directory-in-ubuntu
def getShortPath(p):
	realpath = path.realpath(p).split("/")[1:]
	homepath = path.expanduser("~").split("/")[1:]
	if realpath[:2] == homepath:
		processed = "~"
		realpath = realpath[2:]
	else: processed = "/"
	for i in realpath:
		processed = path.join(processed,i)
	return processed

def getRealPath(p):
	return path.realpath(path.expanduser(p))

def updateCWDVars(p):
	fullpath = getRealPath(p)
	LanguageControls.VARIABLES["CWD"] = ["s",fullpath]
	LanguageControls.VARIABLES["SCWD"] = ["s",getShortPath(p)]

def chdir(p):
	fullpath = getRealPath(p)
	os.chdir(fullpath)
	updateCWDVars(fullpath)