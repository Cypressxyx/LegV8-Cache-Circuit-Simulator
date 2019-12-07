"""
Definition: A memory class that contains 1 blocks of memeory
	0: 000 
	1: 001
	2: 010
	3: 011
	4: 100
	5: 101
	6: 110
	7: 111

Capacity miss: item has been in the cache, but space was tight and it was forced out.
Conflict miss: item was in the cache, but the cache was not associative enough, so it was forced out.
Compulsory miss: item has never been in the cache.
"""
from MemoryModule.memory import Memory
from MemoryModule.memory_tools import parse_memory_location_five_bits, parse_memory_location_8_bits
from MemoryModule.memory_block import MemoryBlock1Kb, MemoryBlock16Kb

class Memory1Kb(Memory):

	def __init__(self):
		self.memory_blocks = {i : MemoryBlock1Kb() for i in range(8)} # Create memory blocks with index 0 - 3
		super().__init__()


	# Load a cached value from memory if exist else store
	def load(self, value):
		index, key   = parse_memory_location_five_bits(value)
		memory_block = self.memory_blocks[index]
		if memory_block.is_on():
			if memory_block.same_key(key):
				return memory_block.get_memory()
			self.misses.conflict += 1
		else:
			self.misses.compulsory += 1
		memory_block.set_key(key)

"""
Definition: A memory class that contains 8 blocks of memeory
|----------|
|xx|xxx|xxx|
|----------|
tag, index, offset
"""
class Memory16Kb(Memory):

	def __init__(self):
		self.memory_blocks = {i : MemoryBlock16Kb() for i in range(9)}
		super().__init__()

	def load(self, value):
		tag, index, offset = parse_memory_location_8_bits(value)
		memory_block   = self.memory_blocks[index]
			
		if memory_block.is_on():
			if memory_block.same_key(offset, tag):
				return memory_block.get_memory(offset)
			self.misses.conflict += 1
		else:
			self.misses.compulsory += 1
		print(index)
		memory_block.set_key(index, tag)
