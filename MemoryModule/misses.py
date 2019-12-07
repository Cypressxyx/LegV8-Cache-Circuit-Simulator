from dataclasses import dataclass

"""
Defintion: A Dataclass that defines misses
	Capacity miss: item has been in the cache, but space was tight and it was forced out.
	Conflict miss: item was in the cache, but the cache was not associative enough, so it was forced out.
	Compulsory miss: item has never been in the cache.
"""
@dataclass
class Misses:
	conflict: int
	capacity: int
	compulsory: int
