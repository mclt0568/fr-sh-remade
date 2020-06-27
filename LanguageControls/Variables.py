import os

def getEnvironment():
	return os.environ

def parsePaths(raw):
	rawSplit = raw.split(":")
	p = []
	for i in rawSplit:
		if os.path.isdir(i):
			p.append(i)
	return p

#type: n = num, s = string, e = environ(non-specify), b = boolean
def parseToFRVAR():
	environ = os.environ
	f = {}
	for i in environ:
		value = ["e",environ[i]]
		f[i] = value
	return f