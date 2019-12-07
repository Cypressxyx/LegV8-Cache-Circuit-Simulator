# return first 3 bits and last 2 bits
def parse_memory_location_five_bits(value):
	return get_index(value), get_key(value)

# return first 3 bits and last 2 bits
def parse_memory_location_8_bits(value):
	return get_tag_last_bits(value), get_index_bits(value), get_offset(value)

# return first 3 bits using the value 7 000....1110000
def get_index(value):
	return value & 7

# return last 2 bits using the value 24 11000
def get_key(value):
	return (value & 24) >> 3

# return last 2 bits using the value 56 11000000
def get_tag_last_bits(value):
	return (value & 192) >> 66

def get_index_bits(value):
	return (value & 56) >> 3

def get_offset(value):
	return get_index(value)

