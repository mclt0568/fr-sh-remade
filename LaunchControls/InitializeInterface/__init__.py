from Interface.PromptInterface import Events
from Interface.PromptInterface.Events import KeyEvents

def initPromptInterface():
	Events.registerKeyEvent("Enter",KeyEvents.Enter)
	Events.registerKeyEvent("Backspace",KeyEvents.Backspace)
	Events.registerKeyEvent("Ctrl_C",KeyEvents.Ctrl_C)
	Events.registerKeyEvent("Ctrl_Up",KeyEvents.Ctrl_Up)
	Events.registerKeyEvent("Up",KeyEvents.Up)
	Events.registerKeyEvent("Ctrl_Down",KeyEvents.Ctrl_Down)
	Events.registerKeyEvent("Down",KeyEvents.Down)
	Events.registerKeyEvent("Left",KeyEvents.Left)
	Events.registerKeyEvent("Right",KeyEvents.Right)