"""
 Defintion: Class Based implementation of a memory block cache
	
 Memory Block defined as having:
		- Key
		- V Value (on or off)
		- Memory Location
		- Index
"""


class MemoryBlock:
	def __init__(self):
		self.key    = None
		self.memory = None
		self.on    = False

	def is_on(self):
		return self.on

	def set_key(self, value):	
		self.on  = True
		self.key = value

	def get_key(self):
		return self.key
	
	def same_key(self, _key):
		return self.key == _key

	def get_memory(self):
		return self.memory
	
