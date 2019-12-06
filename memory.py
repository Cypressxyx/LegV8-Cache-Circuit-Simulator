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
"""
from memory_block import MemoryBlock


class Memory:

	def __init__(self):
		self.memory_blocks = {i : MemoryBlock() for i in range(8)} # Create memory blocks with index 0 - 3

	# Load a cached value from memory if exist else store
	def load(self, memory_location):
		index, key   = self.parse_memory_location(memory_location)
		memory_block = self.memory_blocks[index]
		if memory_block.is_on() and memory_block.same_key(key):	
			print("hey")
			return memory_block.get_memory()
		else:
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
		
