import YTScript

#int str bool float 

def v_int(v):
	try:
		int(v)
		return True
	except Exception:
		return False

def v_float(v):
	try:
		float(v)
		return True
	except Exception:
		return False

def v_str(v):
	try:
		str(v)
		return True
	except Exception:
		return False

def v_bool(v):
	try:
		int(v)
		return True
	except Exception:
		return False

validations = {
	"int":v_int,
	"float":v_float,
	"bool":v_bool,
	"str":v_str
}
converts={
	"int":lambda x: int(x),
	"bool":lambda x: bool(x),
	"float":lambda x: float(x),
	"str":lambda x: str(x)
}
operations={
	"+",lambda x,y : x+y,
	"-",lambda x,y : x-y,
	"*",lambda x,y : x*y,
	"/",lambda x,y : x/y,
	"^",lambda x,y : x^y,
	"%",lambda x,y : x%y,
}
types={
	str(int):"int",
	str(bool):"bool",
	str(float):"float",
	str(str):"str",
}

def convertVariables(t,v):
	return converts[t](v)

def calculateVariable(a,b,o):
	return operations[o](a,b)

def validateVariables(t,v):
	return validations[t](v)

def setVariable(name,t,v):
	YTScript.VARIABLES[name] = [t,v]