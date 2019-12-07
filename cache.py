"""
Test the cache using example
From Class
There should only be a few misses 8 / 24? 
"""
from MemoryModule.memory_types import Memory1Kb

mem = Memory1Kb()
for i in range(2):
	for j in range(10):
		mem.load(j)
print(mem.get_misses())
