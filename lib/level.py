'''Levels constants for the Twisted Twister game'''
class Level():
	def __init__(self):
		self.level = 1
		self.levels = [0,0,0,0,0,0,0]
		self.enemies = []
		self.set_level()

	def start(self):
		self.level = 1
		self.levels = [0,0,0,0,0,0,0]
		self.enemies = []
		self.set_level()

	def next_level(self):
		self.level = self.level + 1
		self.enemies = []
		self.set_level()
	
	def set_level(self):

		'''Complicated algorithm for determining levels'''

		self.levels[0]=(min(8,self.level+6))
		for i in range(1,6):
			self.levels[i]=(self.level/(i*2))

	def get_enemies(self):
		for i in range(6,-1,-1):
			for t in range(0,self.levels[i]):
				self.enemies.append(i)
		return self.enemies

	
	def get_level(self):
		return self.level
