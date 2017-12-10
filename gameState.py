states = {"Start":0, "WaitTranslation": 1}

class GameState:
	def __init__(self):
		self.state = states["Start"]

	def start(self):
		self.state = states["Start"]

	def stop(self):
		self.state = states["Start"]

	def waitTranslation(self):
		self.state = states["WaitTranslation"]

	def setWord(self, word):
		self.word = word