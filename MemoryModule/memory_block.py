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
		self.tag = None

	def is_on(self):
		return self.on
	
	def set_tag(self, _tag):
		self.on  = True
		self.tag = _tag
	
	def get_tag(self):
		return self.tag

	def same_tag(self, _tag):
		return self.get_tag() == _tag
		
class MemoryBlock1Kb(MemoryBlock):
	def __init__(self):	
		self.cell  = MemoryCell()
		super().__init__()

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
	
	def get_memory(self, offset):
		return self.cells[offset].get_memory()

