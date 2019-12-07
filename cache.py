from MemoryModule.memory import Memory1Kb, Memory16Kb

"""
Test the cache using example
From Class
There should only be a few misses 8 / 24? 
"""
mem = Memory1Kb()
memTwo = Memory16Kb()
for i in range(2):
	for j in range(0, 10, 3):
		mem.load(j)
		memTwo.load(j)
print(mem.get_misses())
print(memTwo.get_misses())
