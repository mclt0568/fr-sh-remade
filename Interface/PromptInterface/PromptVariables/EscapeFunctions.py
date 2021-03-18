import LanguageControls
import os
import platform
from Interface.PromptInterface.PromptVariables import escapeVar

@escapeVar("!p")
def fullPath(ctx):
	return LanguageControls.VARIABLES["CWD"][1]

@escapeVar("!s")
def shortPath(ctx):
	return LanguageControls.VARIABLES["SCWD"][1]

@escapeVar("!f")
def currentFolder(ctx):
	return LanguageControls.VARIABLES["CWD"][1].split("/")[-1]

@escapeVar("!h")
def getHostName(ctx):
	return os.uname()[1]

@escapeVar("!o")
def getOsName(ctx):
	return platform.dist()[0]

@escapeVar("!u")
def getUsername(ctx):
	return os.getlogin()