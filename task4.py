from numpy import zeros, random

def sketch(M, k):
	sketches = zeros(shape=(5, 5))
	print k
	print sketches

	rd = random.rand(k) # Random direction
	print rd

sketch([1.0, 2.0, 3.0], 2)
