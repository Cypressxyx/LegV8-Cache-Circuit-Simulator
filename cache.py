"""
Test the cache using example
From Class
There should only be a few misses 8 / 24? 
"""
from memory import Memory

mem = Memory()
for i in range(2):
	for j in range(10):
		mem.load(j)
print(mem.get_misses())
