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
	ctx.commandCarrot = 0

def Backspace(ctx):
	ctx.clearCommandArea()
	sys.stdout.flush()
	if ctx.commandCarrot:
		ctx.command = ctx.command[:ctx.commandCarrot-1] + ctx.command[ctx.commandCarrot:]
		ctx.commandCarrot -= 1

def Ctrl_C(ctx):
	if ctx.command.strip():
		ctx.appendHistory(ctx.command,True)
	sys.stdout.write(f"{ctx.getPrompt()}\033[9m{ctx.command}\033[0m\n")
	sys.stdout.flush()
	ctx.command = ""
	ctx.commandCarrot = 0

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

def Left(ctx):
	if ctx.commandCarrot > 0:
		ctx.commandCarrot -= 1

def Right(ctx):
	if ctx.commandCarrot < len(ctx.command):
		ctx.commandCarrot += 1