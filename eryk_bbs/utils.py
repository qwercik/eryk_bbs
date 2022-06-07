import itertools

def bool_list_to_value(bits):
	# x[0] is exp, x[1] is bit value as boolean
	bits = map(lambda x: (2 ** x[0], x[1]), enumerate(reversed(bits)))
	bits = filter(lambda x: x[1], bits)
	bits = map(lambda x: x[0], bits)
	value = sum(bits)
	return value

def take(n, iterable):
	return list(itertools.islice(iterable, n))

def chunks(n, iterable):
	args = [iter(iterable)] * n
	return zip(*args)

