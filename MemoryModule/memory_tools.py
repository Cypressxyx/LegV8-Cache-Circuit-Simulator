# return first 3 bits and last 2 bits
def parse_memory_location(value):
	return get_index(value), get_key(value)

# return last 3 bits using the value 7 000....1110000
def get_index(value):
	return value & 7

# return last 2 bits using the value 56 000.....111
def get_key(value):
	return value & 56
