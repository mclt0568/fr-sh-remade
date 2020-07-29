def enter(ctx):
	ctx.execCmd(ctx.command)
	ctx.command = ""

def ctrlb(ctx):
	ctx.command += "..."