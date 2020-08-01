import sys
import LanguageControls

def Enter(ctx):
	print("")
	ctx.appendHistory(ctx.command,False)
	ctx.execCmd(ctx.command)
	ctx.command = ""

def Backspace(ctx):
	sys.stdout.write("\r"+(" " * len(f"{ctx.getPrompt()}{ctx.command}")))
	sys.stdout.flush()
	if ctx.command:
		ctx.command = ctx.command[:-1]

def Ctrl_C(ctx):
	ctx.appendHistory(ctx.command,True)
	sys.stdout.write("\r"+(" " * len(f"{ctx.getPrompt()}{ctx.command}")))
	sys.stdout.flush()
	ctx.command = ""

def Up(ctx):
	print("up")

def Ctrl_Up(ctx):
	print("ctrl up")
