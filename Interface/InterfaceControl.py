from Interface import REGISTEREDMODE

def RegisterInterface(name,interfaceClass):
	REGISTEREDMODE[name] = interfaceClass;

def RemoveInterface(name):
	del REGISTEREDMODE[name]