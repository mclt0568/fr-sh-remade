import sys
import LanguageControls

def enter(ctx):
	ctx.execCmd(ctx.command)
	ctx.command = ""

def backspace(ctx):
	sys.stdout.write("\r"+(" " * len(f"{LanguageControls.VARIABLES['PROMPT'][1].replace('!p',LanguageControls.VARIABLES['CWD'][1])}{ctx.command}")))
	if ctx.command:
		ctx.command = ctx.command[:-1]