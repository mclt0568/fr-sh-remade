class Exception:
	self.t = ""
	self.message = ""
	self.line = ""
	def __init__(self,m,l):
		self.message = m
		self.line = l
	def __str__(self):
		return f"An exception has occured\n\tline {self.line}\n\t[{self.t}]{self.message}"

class SyntaxException(Exception):
	self.t = "Syntax"

class TypeException(Exception):
	self.t = "Type"

class NameException(Exception):
	self.t = "Name"

class ArgumentException(Exception):
	self.t = "Arg"