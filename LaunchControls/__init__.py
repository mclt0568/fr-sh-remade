from LaunchControls import InitialVariables
from LaunchControls import InitializeInterface
from os.path import isdir
from Interface import InterfaceControl,PromptInterface
import Interface
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
	CWD = getDefaultPath(LanguageControls.VARIABLES["CWD"][1])
	LanguageControls.VARIABLES["CWD"][1] = CWD
	CWD = CWD.replace(os.path.expanduser("~"),"~")
	LanguageControls.VARIABLES["SCWD"] = ["s",CWD]
	InterfaceControl.RegisterInterface("prompt",PromptInterface.PromptInterface)
	Interface.MODE="prompt"

	#Register Events and Stuff
	InitializeInterface.initPromptInterface()

	#Launch Interface
	Interface.display()

def launchWithMode():
	pass