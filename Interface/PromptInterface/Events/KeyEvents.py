import sys
import LanguageControls

def Enter(ctx):
	print("")
	if ctx.command.strip():
		ctx.appendHistory(ctx.command,False)
	else:
		ctx.commandHistory.resetIndex()
	ctx.execCmd(ctx.command)
	ctx.command = ""

def Backspace(ctx):
	ctx.clearCommandArea()
	sys.stdout.flush()
	if ctx.command:
		ctx.command = ctx.command[:-1]

def Ctrl_C(ctx):
	ctx.appendHistory(ctx.command,True)
	ctx.clearCommandArea()
	sys.stdout.flush()
	ctx.command = ""

def Up(ctx):
	ctx.clearCommandArea()
	ctx.command = ctx.commandHistory.getPrevHistory(False)[0]

def Ctrl_Up(ctx):
	ctx.clearCommandArea()
	ctx.command = ctx.commandHistory.getPrevHistory(True)[0]

def Down(ctx):
	ctx.clearCommandArea()
	ctx.command = ctx.commandHistory.getNextHistory(False)[0]

def Ctrl_Down(ctx):
	ctx.clearCommandArea()
	ctx.command = ctx.commandHistory.getNextHistory(True)[0]
