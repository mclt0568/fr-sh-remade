import os
from os import walk
from LanguageControls import Variables
import LanguageControls

def getFiles(path):
	f = []
	for (dp, di, fn) in walk(path):
		f.extend(fn)
		break
	return f

def getExecutableList(path):
	e = []
	f = getFiles(path)
	for i in f:
		if os.access(os.path.join(path,i), os.X_OK):
			e.append(i)
	return e