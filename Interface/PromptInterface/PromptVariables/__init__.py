ESCAPES = {
	"!e": lambda ctx:"!",
}

def registerEscapes(escape,function):
	ESCAPES[escape] = function

def escapeVar(e):
	def wrapper(func):
		ESCAPES[e] = func
		return func
	return wrapper

def getPrompt(ctx,prompt):
	for i in ESCAPES:
		while i in prompt:
			prompt = prompt.replace(i,ESCAPES[i](ctx))
	return prompt