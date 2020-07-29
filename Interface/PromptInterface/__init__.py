from Interface.PromptInterface import Events
from sys import stdout
from Interface import GetKeyPress
import LanguageControls
import readchar
import sys


class PromptInterface:
	def __init__(self):
		self.commandhistory = []
		self.command = ""
	def prevHistory(self,hidden):
		pass
	def nextHistory(self,hidden):
		pass
	def appendHistory(self,cmd,hidden):
		if not cmd.strip() == "":
			self.commandhistory.append([cmd,hidden])
		#print(self.commandhistory) 
	def execCmd(self,cmd):
		if cmd.lower().strip() == "exit":
			sys.exit()
		print(f"\nUnknown CMD: {cmd}")
	def getPrompt(self):
		prompt = f"\r{LanguageControls.VARIABLES['PROMPT'][1]}"
		while "!p" in prompt:
			prompt = prompt.replace("!p",LanguageControls.VARIABLES["CWD"][1])
		while "!s" in prompt:
			prompt = prompt.replace("!s",LanguageControls.VARIABLES["SCWD"][1])
		return prompt
	def execute(self):
		while True:
			stdout.write(f"{self.getPrompt()}{self.command}")
			k = GetKeyPress.listen()
			if k in Events.KEYPRESS_EVENTS:
				Events.KEYPRESS_EVENTS[k](self)
			else:
				self.command+=k
