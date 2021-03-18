KEYPRESS_EVENTS = {}

def registerKeyEvent(c,e):
	KEYPRESS_EVENTS[c] = e

def keyEvent(c):
	def wrapper(func):
		KEYPRESS_EVENTS[c] = func
		return func
	return wrapper
