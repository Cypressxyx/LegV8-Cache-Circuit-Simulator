# return first 3 bits and last 2 bits
def parse_memory_location_five_bits(value):
	tag   = get_bits(value, 2, 2)
	index = get_bits(value, 3, 0)
	return index, tag

# returna index tag and offset in a value 
def parse_memory_location_8_bits(value):
	tag    = get_bits(value, 2, 6)
	index  = get_bits(value, 3, 3)
	offset = get_bits(value, 3, 0)
	return tag, index, offset

# return the nth bits 
def get_bits(value, num_bits, starting_position):
	mask = 1
	for i in range(1, num_bits):	
		mask = mask << 1 | 1
	mask = mask << starting_position
	return (value & mask) // (2**starting_position)