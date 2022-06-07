import math
from .utils import chunks, bool_list_to_value

def dist_nbits(gen, n):
	bits = chunks(n, gen)
	return map(bool_list_to_value, bits)

def dist_byte(gen):
	return dist_nbits(gen, 8)

# It's not safe int distribution due to a bias!
def dist_int(gen, rng):
	start, end = rng
	size = end - start
	nbits = math.ceil(math.log2(size))

	rand = dist_nbits(gen, nbits)
	return map(lambda r: start + (r % size), rand)

