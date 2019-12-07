from MemoryModule.misses import Misses
class Memory:
	def __init__(self):
		self.misses = Misses(0, 0, 0)

	def get_misses(self):
		return self.misses


