from MemoryModule.misses import Misses
from MemoryModule.memory_tools import parse_memory_location_five_bits, parse_memory_location_8_bits
from MemoryModule.memory_block import MemoryBlock1Kb, MemoryBlock16Kb

"""
Definition: A memory parent class 
"""
class Memory:
	def __init__(self):
		self.misses = Misses(0, 0, 0)

	def get_misses(self):
		return self.misses

"""
Definition: A memory class that contains 1 blocks of memory
"""
class Memory1Kb(Memory):

	def __init__(self):
		self.memory_blocks = {i : MemoryBlock1Kb() for i in range(8)} # Create memory blocks with index 0 - 3
		super().__init__()


	# Load a cached value from memory if exist else store
	def load(self, value):
		index, tag   = parse_memory_location_five_bits(value)
		memory_block = self.memory_blocks[index]
		if memory_block.is_on():
			if memory_block.same_tag(tag):
				return memory_block.get_memory()
			self.misses.conflict += 1
		else:
			self.misses.compulsory += 1
		memory_block.set_tag(tag)

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
			if memory_block.same_tag(tag):
				return memory_block.get_memory(offset)
			self.misses.conflict += 1
		else:
			self.misses.compulsory += 1
		memory_block.set_tag(tag)
