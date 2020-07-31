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

def preInit():
	InitialVariables.read()

def init(mode,cwd):
	CWD = getDefaultPath(cwd)
	LanguageControls.VARIABLES["CWD"][1] = CWD
	CWD = CWD.replace(os.path.expanduser("~"),"~")
	LanguageControls.VARIABLES["SCWD"] = ["s",CWD]
	InterfaceControl.RegisterInterface(mode,PromptInterface.PromptInterface)
	Interface.MODE=mode

def launch():
	preInit()
	init("prompt",LanguageControls.VARIABLES["CWD"][1])

	#Register Events and Stuff
	InitializeInterface.initPromptInterface()

	#Launch Interface
	Interface.display()

def launchWithMode(mode):
	pass

def launchWithScript(filename):
	pass
