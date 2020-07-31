from LanguageControls import Variables
import LanguageControls,json
from os.path import join as pathjoin
from os.path import dirname
import sys

def read():
	LanguageControls.VARIABLES = Variables.parseToFRVAR()
	with open(pathjoin(".","defaultVariables.json"),"r") as f:
		defaultJson = json.load(f)
	for i in defaultJson:
		v = defaultJson[i]
		LanguageControls.VARIABLES[i] = v