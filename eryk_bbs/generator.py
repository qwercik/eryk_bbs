#!/usr/bin/env python3

import sys
import math
import numpy as np
from itertools import cycle
from functools import wraps
from app.utils import take, chunks

p = 3103559279
q = 1265734819
k = 3
seed = 914982490343715292

def lsb(raw_gen):
	@wraps(raw_gen)
	def wrapper(*args, **kwargs):
		return map(lambda x: bool(x & 1), raw_gen(*args, **kwargs))
	return wrapper

def bit_cycle(raw_gen):
	@wraps(raw_gen)
	def wrapper(*args, **kwargs):
		bit_index = cycle(range(4))
		gen = raw_gen(*args, **kwargs)
		return map(lambda x: bool((x[1] >> x[0]) & 1), zip(bit_index, gen))
	return wrapper

def measure_cycle(gen):
	@wraps(gen)
	def wrapper(*args, **kwargs):
		raw_gen = gen.__wrapped__(*args, **kwargs)
		ocurred = set()
		try:
			while True:
				value = next(raw_gen)
				if value in ocurred:
					break
				ocurred.add(value)
		except KeyboardInterrupt:
			pass

		return len(ocurred)
	return wrapper

@lsb
def bbs(n=p*q, seed=seed):
	x = seed ** 2 % n
	while True:
		yield x 
		x = x ** 2 % n

bbs_bc = bit_cycle(bbs.__wrapped__)


@lsb
def mygen(n=p*q, seed=seed, k=k):
	x = pow(seed, k, n)
	while True:
		yield x
		x = pow(x, k, n)

@lsb
def langton(size=100, k=5):
	def ant(matrix, position, direction):
		height, width = matrix.shape
		y, x = position
		dy, dx = direction

		while True:
			yield (y, x)
			y = (y + dy) % height
			x = (x + dx) % width

			dy, dx = dx, dy
			if matrix[y, x] == 0 and dx == 0:
				dy *= -1
			elif matrix[y, x] == 1 and dy == 0:
				dx *= -1

	matrix = np.zeros((size, size))
	ants = [ant(matrix, (20, 20), (-1, 0))]
	while True:
		v = 0
		for _ in range(k):
			positions = next(zip(*ants))
			for y, x in positions:
				print(y, x, file=sys.stderr)
				v += y * x
				matrix[y][x] = 1 if matrix[y][x] == 0 else 0

		yield v & 1

