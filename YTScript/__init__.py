import YTScript.Variables
from YTScript import Commands
from YTScript import Exceptions

VARIABLES = {}

class interpreter:
	def __init__(self,interface):
		self.i = interface
		self.cmds = {"INIT":Commands.INIT,"OUTPUTLN":Commands.OUTPUTLN,"OUTPUT":Commands.OUTPUT,"OUTPUTNL":Commands.OUTPUTNL,"OUTPUTVAR":Commands.OUTPUTVAR,"SETVAR":Commands.SETVAR,"SETVARMATH":Commands.SETVARMATH,"COPYVAR":Commands.COPYVAR,"INPUTVAR":Commands.INPUTVAR,"GOTO":Commands.GOTO,"EXIT":Commands.EXIT}
	def execute(self,command):
		pass
	def throw(self,e):
		print(e)