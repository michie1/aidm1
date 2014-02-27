def minhash(S, k):
	print list(set().union(*S))

minhash([ [1, 2, 3], [3, 4, 5] ], 3)

#and returns two objects: a sorted list of all strings that occur in S
# Sorted how?
