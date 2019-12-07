"""
Definition: A memory class that contains 8 blocks of memeory
	0: 000 
	1: 001
	2: 010
	3: 011
	4: 100
	5: 101
	6: 110
	7: 111

Compulsory miss: item has never been in the cache.
Capacity miss: item has been in the cache, but space was tight and it was forced out.
Conflict miss: item was in the cache, but the cache was not associative enough, so it was forced out.
"""
from memory_block import MemoryBlock


class Memory:

	def __init__(self):
		self.memory_blocks = {i : MemoryBlock() for i in range(8)} # Create memory blocks with index 0 - 3
		self.num_compulsory_miss = 0
		self.misses = { "compulsory": 0, 
										"capacity": 0, 
										"conflict": 0 }

	# Load a cached value from memory if exist else store
	def load(self, memory_location):
		index, key   = self.parse_memory_location(memory_location)
		memory_block = self.memory_blocks[index]
		if memory_block.is_on():
			if memory_block.same_key(key):
				return memory_block.get_memory()
			self.misses["conflict"] += 1
		else:
			self.misses["compulsory"] += 1
		memory_block.set_key(key)
			
	# return first 3 bits and last 2 bits
	def parse_memory_location(self, value):	
		return self.get_index(value), self.get_key(value)

	# return last 2 bits
	def get_key(self, value):
		return value & 56 # binary: 000....1110000

	# Return first 3 bits
	def get_index(self, value):
		return value & 7 # 000000....111
	
	def get_misses(self):
		return self.misses
		
