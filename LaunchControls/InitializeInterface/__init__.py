from Interface.PromptInterface import Events
from Interface.PromptInterface.Events import KeyEvents

def initPromptInterface():
	Events.registerKeyEvent("Enter",KeyEvents.enter)
	Events.registerKeyEvent("Backspace",KeyEvents.backspace)
	Events.registerKeyEvent("Ctrl_C",KeyEvents.ctrl_c)