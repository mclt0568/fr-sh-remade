import sys
import LanguageControls

def enter(ctx):
	ctx.appendHistory(ctx.command,False)
	ctx.execCmd(ctx.command)
	ctx.command = ""

def backspace(ctx):
	sys.stdout.write("\r"+(" " * len(f"{ctx.getPrompt()}{ctx.command}")))
	if ctx.command:
		ctx.command = ctx.command[:-1]

def ctrl_c(ctx):
	ctx.appendHistory(ctx.command,True)
	sys.stdout.write("\r"+(" " * len(f"{ctx.getPrompt()}{ctx.command}")))
	ctx.command = ""