#INIT|OUTPUTLN|OUTPUT|OUTPUTNL|OUTPUTVAR|SETVAR|SETVARMATH|COPYVAR|INPUTVAR|GOTO|EXIT|SLEEP|OS|SCRIPT|IF
import YTScript
import sys
import time
from YTScript import Exceptions
from YTScript import Variables

def INIT(ctx,args):
	YTScript.Variables = {}

def OUTPUTLN(ctx,args):
	a = ""
	for i in args:
		a += i + " "
	a = a[:-1]
	print(a)
	return None

def OUTPUT(ctx,args):
	a = ""
	for i in args:
		a += i + " "
	a = a[:-1] 
	sys.stdout.write()
	sys.stdout.flush()
	return None

def OUTPUTNL(ctx,args):
	print()
	return None

def OUTPUTVAR(ctx,args):
	if args[0][1] in YTScript.VARIABLES:
		sys.stdout.write(args[0][1])
		sys.stdout.flush()
	return None

def SETVAR(ctx,args):
	if (not(len(args) == 3)): return Exceptions.ArgumentException(f"Expect 3, gets {len(args)}",args)
	if not(Variables.validateVariables(args[1],args[2])): return Exceptions.TypeException(f"Unable to convert {args[2]} into {args[1]}",args)
	Variables.setVariable(args[0],args[1],Variables.convertVariable(args[1],args[2]))
	return None

def SETVARMATH(ctx,args):
	if (not(len(args) == 4)): return Exceptions.ArgumentException(f"Expect 4, gets {len(args)}",args)
	if not (args[2] in Variables.operation): return Exceptions.ArgumentException(f"{args[2]} is not a valid operator",args)
	if not (args[1] in YTScript.VARIABLES): return Exceptions.NameException(f"{args[1]} does not exist",args) 
	if not (args[3] in YTScript.VARIABLES): return Exceptions.NameException(f"{args[3]} does not exist",args)
	try:
		result = Variables.operations(args[1],args[3])
	except TypeError:
		return Exceptions.TypeException(f"{args[2]} operation does not support between {args[1]} and {args[3]}",args)
	Variables.setVariable(args[0],Variables.types[str(type(result))],result)
	return None

def COPYVAR(ctx,args):
	if (not(len(args) == 2)): return Exceptions.ArgumentException(f"Expect 2, gets {len(args)}",args)
	if not (args[1] in YTScript.VARIABLES): return Exceptions.NameException(f"{args[1]} does not exist",args) 

def INPUTVAR(ctx,args):
	pass

def GOTO(ctx,args):
	pass

def EXIT(ctx,args):
	sys.exit()

def SLEEP