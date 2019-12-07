from dataclasses import dataclass

@dataclass
class Misses:
	conflict: int
	capacity: int
	compulsory: int
