from Interface.PromptInterface import Events
from LaunchControls.InitializeInterface import PromptInterfaceKeyEvents

def initPromptInterface():
	Events.registerKeyEvent("\r",PromptInterfaceKeyEvents.enter)
	Events.registerKeyEvent("\x02",PromptInterfaceKeyEvents.ctrlb)