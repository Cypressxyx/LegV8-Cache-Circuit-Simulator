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
from MemoryModule.misses import Misses
from MemoryModule.memory_tools import parse_memory_location
from MemoryModule.memory_block import MemoryBlock, MemoryBlock16Kb

class Memory:
	def __init__(self):
		self.memory_blocks = {i : MemoryBlock() for i in range(8)} # Create memory blocks with index 0 - 3
		self.misses        = Misses(0, 0, 0)

	# Load a cached value from memory if exist else store
	def load(self, memory_location):
		index, key   = parse_memory_location(memory_location)
		memory_block = self.memory_blocks[index]
		if memory_block.is_on():
			if memory_block.same_key(key):
				return memory_block.get_memory()
			self.misses.conflict += 1
		else:
			self.misses.compulsory += 1
		memory_block.set_key(key)
			
	def get_misses(self):
		return self.misses


class Memory16Kb:

	def __init__(self):
		self.memory_blocks = {i : MemoryBlock16Kb() for i in range(8)}
		self.misses        = Misses(0, 0, 0)
	
