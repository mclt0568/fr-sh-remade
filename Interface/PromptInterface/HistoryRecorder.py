class HistoryRecorder:
	def __init__(self):
		self.index = 0
		self.history = []
	def resetIndex(self):
		self.index = 0
	def getCurrentHistory(self):
		if self.index:
			return self.history[self.index-1]
		return ["",False]
	def nextIndex(self):
		if self.index == len(self.history):
			self.index == 0
			return
		elif self.index == 0:
			return
		self.index += 1
	def prevIndex(self):
		if self.index == 0:
			self.index = len(self.history)
			return
		elif self.index == 1:
			return
		self.index -= 1
	def append(self,command,isHidden):
		self.history.append([command,isHidden])
		self.resetIndex()
	def getPrevHistory(self,isHidden):
		if isHidden:
			self.prevIndex()
			return self.getCurrentHistory()
		else:
			while True:
				self.prevIndex()
				temp = self.getCurrentHistory()
				if not temp[1]:
					return temp

	def getNextHistory(self,isHidden):
		if isHidden:
			self.nextIndex()
			return self.getCurrentHistory()
		else:
			while True:
				self.nextIndex()
				temp = self.getCurrentHistory()
				if not temp[1]:
					return temp