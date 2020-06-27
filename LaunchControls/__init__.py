from LaunchControls import InitialVariables
from os.path import isdir
import LanguageControls
import os

def getDefaultPath(path):
	cwd = os.getcwd()
	if path:
		if isdir(path):
			return path
		return cwd
	return cwd

def launch():
	InitialVariables.read()
	LanguageControls.VARIABLES["CWD"] = getDefaultPath(LanguageControls.VARIABLES["CWD"][1])