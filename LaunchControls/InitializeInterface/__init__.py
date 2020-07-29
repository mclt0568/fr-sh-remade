from Interface.PromptInterface import Events
from Interface.PromptInterface.Events import KeyEvents

def initPromptInterface():
	Events.registerKeyEvent("Enter",KeyEvents.Enter)
	Events.registerKeyEvent("Backspace",KeyEvents.Backspace)
	Events.registerKeyEvent("Ctrl_C",KeyEvents.Ctrl_C)
	Events.registerKeyEvent("Ctrl_Up",KeyEvents.Ctrl_Up)
	Events.registerKeyEvent("Up",KeyEvents.Up)