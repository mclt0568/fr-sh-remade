from Interface import GetKeyPress
from Interface.YTScript import Events
from Interface.YTScript.Events import KeyEvents
from Interface.YTScript.HistoryRecorder import HistoryRecorder
from sys import stdout
import LanguageControls
import DirControls
import readchar
import sys
import os

def RegisterDefaultEvents():
	Events.registerKeyEvent("Enter",KeyEvents.Enter)
	Events.registerKeyEvent("Backspace",KeyEvents.Backspace)
	Events.registerKeyEvent("Ctrl_C",KeyEvents.Ctrl_C)
	Events.registerKeyEvent("Ctrl_Up",KeyEvents.Ctrl_Up)
	Events.registerKeyEvent("Up",KeyEvents.Up)
	Events.registerKeyEvent("Ctrl_Down",KeyEvents.Ctrl_Down)
	Events.registerKeyEvent("Down",KeyEvents.Down)
	Events.registerKeyEvent("Left",KeyEvents.Left)
	Events.registerKeyEvent("Right",KeyEvents.Right)

RegisterDefaultEvents()

class YSInterface:
	def __init__(self):
		self.commandHistory = HistoryRecorder()
		self.command = ""
		self.commandCarrot = 0
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
					if os.path.isdir(DirControls.getRealPath(args[0])):
						path = DirControls.getRealPath(args[0])
						DirControls.chdir(path)
						# LanguageControls.VARIABLES["CWD"] = path
						# path = path.replace(os.path.expanduser("~"),"~")
						# LanguageControls.VARIABLES["SCWD"] = ["s",path]
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
		return "\rYTScript>"
		return prompt
	def setCarrot(self,index):
		stdout.write(f"{self.getPrompt()}{self.command}")
		stdout.flush()
		stdout.write(f"{self.getPrompt()}{self.command[:self.commandCarrot]}")
		stdout.flush()
	def execute(self):
		while True:
			self.setCarrot(self.commandCarrot)
			k = GetKeyPress.listen()
			# print(Events.KEYPRESS_EVENTS)
			# print(k)
			# print(k in Events.KEYPRESS_EVENTS)
			if k in Events.KEYPRESS_EVENTS:
				Events.KEYPRESS_EVENTS[k](self)
			elif (k.isprintable()) and (len(k) == 1):
				self.command = self.command[:self.commandCarrot] + k + self.command[self.commandCarrot:]
				self.commandCarrot += 1