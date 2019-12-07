from memory import Memory

"""
Test the cache using example
From Class
There should only be a few misses 8 / 24? 
"""
mem = Memory()
for i in range(2):
	for j in range(10):
		mem.load(j)

print(mem.get_misses())
"""
def test_cache():
	for i in range(2):
		for j in range(23):
			print(j)
			#check_hit_or_miss(j)

"""
