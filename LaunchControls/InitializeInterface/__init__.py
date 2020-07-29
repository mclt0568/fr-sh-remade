from Interface.PromptInterface import Events
from Interface.PromptInterface.Events import KeyEvents

def initPromptInterface():
	Events.registerKeyEvent("\r",KeyEvents.enter)
	Events.registerKeyEvent("\x7f",KeyEvents.backspace)