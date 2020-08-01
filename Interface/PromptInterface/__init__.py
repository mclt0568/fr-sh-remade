from Interface.PromptInterface import Events
from sys import stdout
from Interface import GetKeyPress
import LanguageControls
import readchar
import sys
import os


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
		# if cmd.lower().strip() == "exit":
		# 	print("\n")
		# 	sys.exit()
		# else:
		# 	#only for test puporse
		# 	cmdstrip = cmd.strip().split(" ")
		# 	cmdfinal = ""
		# 	for i in cmdstrip:
		# 		cmdfinal += i + " "
		# 	os.system(cmdfinal)
		# 	#print(f"\nUnknown CMD: {cmd}")
		if cmd.lower().strip():
			os.system(cmd)
		else:
			sys.exit()
	def getPrompt(self):
		prompt = f"\r{LanguageControls.VARIABLES['PROMPT'][1]}"
		while "!p" in prompt:
			prompt = prompt.replace("!p",LanguageControls.VARIABLES["CWD"][1])
		while "!s" in prompt:
			prompt = prompt.replace("!s",LanguageControls.VARIABLES["SCWD"][1])
		while "!c" in prompt:
			prompt = prompt.replace("!c","\033[")
		return prompt
	def execute(self):
		while True:
			stdout.write(f"{self.getPrompt()}{self.command}")
			stdout.flush()
			k = GetKeyPress.listen()
			if k in Events.KEYPRESS_EVENTS:
				Events.KEYPRESS_EVENTS[k](self)
			elif (k.isprintable()) and (len(k) == 1):
				self.command+=k
