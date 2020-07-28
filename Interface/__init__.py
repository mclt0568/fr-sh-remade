MODE = ""
REGISTEREDMODE = {}
CURRENTCLASS = None

def display():
	#display base on mode
	CURRENTCLASS = REGISTEREDMODE[MODE]()
	CURRENTCLASS.execute()
	# print("Place Holder: Interface.(__init__).display()")