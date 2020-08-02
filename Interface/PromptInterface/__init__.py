from Interface.PromptInterface import Events
from Interface.PromptInterface.HistoryRecorder import HistoryRecorder
from sys import stdout
from Interface import GetKeyPress
import LanguageControls
import readchar
import sys
import os

class PromptInterface:
	def __init__(self):
		self.commandHistory = HistoryRecorder()
		self.command = ""
	def appendHistory(self,cmd,hidden):
		if not cmd.strip() == "":
			self.commandHistory.append(cmd,hidden)
	def clearCommandArea(self):
		sys.stdout.write("\r"+(" " * len(f"{self.getPrompt()}{self.command}")))
		sys.stdout.flush()
	def execCmd(self,cmd):
		processed = cmd.strip().split(" ")
		#Just for testing purpose, will add language parsing and other things after planning
		if processed:
			args = processed[1:]
			if processed[0] == "cd":
				if args:
					if os.path.isdir(args[0]):
						path = os.path.abspath(args[0])
						os.chdir(path)
						LanguageControls.VARIABLES["CWD"] = path
						path = path.replace(os.path.expanduser("~"),"~")
						LanguageControls.VARIABLES["SCWD"] = ["s",path]
					else:
						print(f"[fr-sh][!] {args[0]} is not a valid directory")
				else:
					print("[fr-sh][!] No Args Provided!")
			elif processed[0] == "exit":
				print("[fr-sh][!] Good Bye!")
				sys.exit()
			else:
				os.system(cmd)
		else:
			print("")
			#Endi of
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
			# print(Events.KEYPRESS_EVENTS)
			# print(k)
			# print(k in Events.KEYPRESS_EVENTS)
			if k in Events.KEYPRESS_EVENTS:
				Events.KEYPRESS_EVENTS[k](self)
			elif (k.isprintable()) and (len(k) == 1):
				self.command+=k