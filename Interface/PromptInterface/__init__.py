from Interface.PromptInterface import Events
from sys import stdout
import LanguageControls
import readchar
import time

class PromptInterface:
	def __init__(self):
		self.commandhistory = []
		self.command = ""
	def prevHistory(self,hidden):
		pass
	def nextHistory(self,hidden):
		pass
	def execCmd(self,cmd):
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
			c = readchar.readkey()
			if c in Events.KEYPRESS_EVENTS:
				Events.KEYPRESS_EVENTS[c](self)
			elif c == "\x03":
				return
			else:
				self.command+=c