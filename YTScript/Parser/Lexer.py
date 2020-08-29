import ply.lex as lex

class Lexer:

	errors = []

	tokens = (
		'COMMAND',
		'ARGUMENTS',
		'DATATYPEKW',
		'QOUTE',

		'INT',
		'FLOAT',
		'BOOL',

		'SPACE',
		'COMMENT',
		# 'PLUS',
		# 'MINUS',
		# 'MULTIPLY',
		# 'DIVIDE',
		# 'POWER',
		# 'MOD',
		# 'EQUAL',
	)

	# t_PLUS    = r'\+'
	# t_MINUS    = r'\-'
	# t_MULTIPLY    = r'\*'
	# t_DIVIDE    = r'\/'
	# t_POWER    = r'\^'
	# t_MOD    = r'\%'
	# t_EQUAL    = r'\='

	def t_SPACE(self,t):
		r"\s"
		pass

	# t_SPACE    = r'\s'

	def t_QOUTE(self,t):
		r'"(?:[^"\\]|\\.)*"'
		t.value = str(t.value)[1:-1]
		return t

	def t_COMMENT(self,t):
		r"\#.*"
		t.value = str(t.value)
		pass
	def t_DATATYPEKW(self,t):
		r'(?<=\s)int|str|bool|INT|STR|BOOL'
		t.value = str(t.value)
		return t

	def t_ARGUMENTS(self,t):
		r'(?<=\s)[a-z|A-Z|0-9|\+|\-|\*|\/|\%|\^|=]'
		t.value = str(t.value)
		return t
	
	def t_COMMAND(self,t):
		r'(?<=\s)INIT|OUTPUTLN|OUTPUT|OUTPUTNL|OUTPUTVAR|SETVAR|SETVARMATH|COPYVAR|INPUTVAR|GOTO|EXIT|SLEEP|OS|SCRIPT|IF'
		# r'(?<!.)[a-z|A-Z]*'
		t.value = str(t.value)
		return t

	def t_error(self,t):
		self.errors.append("Illegal character '%s'" % t.value[0])
		t.lexer.skip(1)

	def build(self,**kwargs):
		self.errors = []
		self.lexer = lex.lex(module=self, **kwargs)

	# Test it output
	def test(self,data):
		self.errors = []
		self.lexer.input(data)
		while True:
			tok = self.lexer.token()
			if not tok: break
			print(tok.value)
			# help(tok)
			# break

	def report(self):
		return self.errors

# m = MyLexer()
# m.build()
# # m.test('OUTPUT "hello # world" #this will print "hello # world"')
# m.test('SETVAR a + 3 INT 1 #this sets a as int with value of 1')
# print(m.report())