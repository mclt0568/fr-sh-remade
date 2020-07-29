from Interface.PromptInterface import Events
import LanguageControls
import readchar

class PromptInterface:
	def __init__(self):
		self.command = ""
	def execute(self):
		while True:
			c = readchar.readkey()
			if c in Events.KEYPRESS_EVENTS:
				Events.KEYPRESS_EVENTS[c](self)
			else:
				return
			print(self.command)