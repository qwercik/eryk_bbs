import math
from itertools import count
from app.generator import mygen
from app.distribution import dist_nbits, dist_int

def generate_prime(bit_width=128):
	gen = mygen()
	candidate = dist_nbits(gen, bit_width)

	randint = lambda s, e: next(dist_int(gen, (s, e)))
	_miller_rabin = lambda c: miller_rabin_primality_test(c, k=5, rand=randint)

	candidate = filter(lambda x: x % 4 == 3, candidate)
	candidate = filter(fermat_primality_test, candidate)
	candidate = filter(_miller_rabin, candidate)

	return candidate

def fermat_primality_test(prime_candidate, base=2):
	return pow(base, prime_candidate - 1, prime_candidate) == 1


# Source and symbols: https://pl.wikipedia.org/wiki/Test_Millera-Rabina
def miller_rabin_primality_test(prime_candidate, k, rand):
	def extract_2_pow(value):
		s = 0
		d = value
		while d % 2 == 0:
			s += 1
			d //= 2
		return (s, d)
	
	s, d = extract_2_pow(prime_candidate - 1)
	for _ in range(k):
		a = rand(1, prime_candidate - 1)
		if pow(a, d, prime_candidate) == 1:
			continue

		for r in range(s):
			if pow(a, (2 ** r) * d, prime_candidate) == -1:
				break
		else:
			return False

	return True


def factorize(value):
	for d in range(2, value + 1):
		while True:
			if value == 1:
				return
			elif value % d == 0:
				value //= d
				yield d
			else:
				break

