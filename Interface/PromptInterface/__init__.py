import LanguageControls

class PromptInterface:
	def __init__(self):
		pass
	def execute(self):
		while True:
			PROMPT = LanguageControls.VARIABLES["PROMPT"][1]
			while "!p" in PROMPT:
				PROMPT = PROMPT.replace("!p",LanguageControls.VARIABLES["CWD"])
			cmd = input(PROMPT)
			if cmd == "exit":
				return