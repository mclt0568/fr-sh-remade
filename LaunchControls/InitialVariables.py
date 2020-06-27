from LanguageControls import Variables
import LanguageControls,json
from os.path import join as pathjoin

def read():
	LanguageControls.VARIABLES = Variables.parseToFRVAR()
	with open(pathjoin(".","LaunchControls","defaultVariables.json"),"r") as f:
		defaultJson = json.load(f)
	for i in defaultJson:
		v = defaultJson[i]
		LanguageControls.VARIABLES[i] = v