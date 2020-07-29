from readchar import readkey

# def initPromptInterface():
# 	Events.registerKeyEvent("\r",KeyEvents.enter)
# 	Events.registerKeyEvent("\x7f",KeyEvents.backspace)
# 	Events.registerKeyEvent("\x03",KeyEvents.ctrl_c)

def listen():
	l1 = {
		"\r":"Enter",
		"\x7f":"Backspace",
		"\x03":"Ctrl_C",
		"\x1b[A":"Up",
		"\x1b[B":"Down",
		"\x1b[C":"Right",
		"\x1b[D":"Left",
	}
	l2 = {

	}
	l3 = {

	}
	l4={
		"\x1b[1":{
			";":{
				"5":{
					"A":"Ctrl_Up",
					"B":"Ctrl_Down",
					"C":"Ctrl_Right",
					"D":"Ctrl_Left",
				}
			}
		}
	}

	c = readkey()
	if c in l1:
		return l1[c]
	elif c in l2:
		c1 = readkey()
		if c1 in l2[c]:
			return l2[c][c1]
		else:
			return ""
	elif c in l3:
		c1 = readkey()
		if c1 in l3[c]:
			c2 = readkey()
			if c2 in l3[c][c1]:
				return l3[c][c1][c2]
			else:
				return ""
		else:
			return ""
	elif c in l4:
		c1 = readkey()
		if c1 in l4[c]:
			c2 = readkey()
			if c2 in l4[c][c1]:
				c3 = readkey()
				if c3 in l4[c][c1][c2]:
					return l4[c][c1][c2][c3]
				else:
					return ""
			else:
				return ""
		else:
			return ""
	elif c.isprintable() and (len(c) == 1) :
		return c
	else:
		return ""