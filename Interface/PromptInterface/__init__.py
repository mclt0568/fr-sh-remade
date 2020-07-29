from Interface.PromptInterface import Events
from sys import stdout
import LanguageControls
import LanguageControls
import readchar

class PromptInterface:
	def __init__(self):
		self.commandhistory = []
		self.command = ""
	def execute(self):
		while True:
			stdout.write(f"\r{LanguageControls.VARIABLES['PROMPT'][1].replace('!p',LanguageControls.VARIABLES['CWD'][1])}{self.command}")
			c = readchar.readkey()
			if c in Events.KEYPRESS_EVENTS:
				Events.KEYPRESS_EVENTS[c](self)
			elif c == "\x03":
				return
			else:
				self.command+=c
			
	def prevHistory(self,hidden):
		pass
	def nextHistory(self,hidden):
		pass
	def execCmd(self,cmd):
		print(f"\nUnknown CMD: {cmd}")