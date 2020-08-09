import LanguageControls
import os
import platform

def fullPath(ctx):
	return LanguageControls.VARIABLES["CWD"][1]

def shortPath(ctx):
	return LanguageControls.VARIABLES["SCWD"][1]

def currentFolder(ctx):
	return LanguageControls.VARIABLES["CWD"][1].split("/")[-1]

def getHostName(ctx):
	return os.uname()[1]

def getOsName(ctx):
	return platform.dist()[0]

def getUsername(ctx):
	return os.getlogin()