from Interface.PromptInterface.PromptVariables import EscapeFunctions

ESCAPES = {
	"!e": lambda ctx:"!",
}

def registerEscapes(escape,function):
	ESCAPES[escape] = function

def getPrompt(ctx,prompt):
	for i in ESCAPES:
		while i in prompt:
			prompt = prompt.replace(i,ESCAPES[i](ctx))
	return prompt