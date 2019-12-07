from MemoryModule.memory_cell import MemoryCell 

"""
 Defintion: Class Based implementation of a memory block cache
						Memory Block defined as having:
							- 1 col cell
							- V Value (on or off)
"""
class MemoryBlock:
	def __init__(self):
		self.on = False

	def is_on(self):
		return self.on


class MemoryBlock1Kb(MemoryBlock):
	def __init__(self):	
		self.cell  = MemoryCell()
		super().__init__()

	def set_key(self, value):	
		self.on  = True
		self.cell.set_key(value)

	def get_key(self):
		return self.cell.get_key()
	
	def same_key(self, _key):
		return self.get_key() == _key

	def get_memory(self):
		return self.cell.get_memory()

"""
 Defintion: Class Based implementation of a memory block cache
						with 16 bits
							- 1 col cell
							- V Value (on or off)
"""
class MemoryBlock16Kb(MemoryBlock):
	def __init__(self):
		self.cells =  {i: MemoryCell() for i in range(8)}
		super().__init__()
	
	def same_key(self, _key):
		return None
		#return self.cell{

	
