from numpy import zeros, random

def minhash(S, k):
	Words = list(set().union(*S)) # Figure 3.2 first column
	Characteristics = zeros(shape=(len(Words), len(S))) # Figure 3.2 bit matrix
	Signatures = zeros(shape=(k, len(S)))

	for i, w in enumerate(Words):
		for j in range(len(S)):
			if w in S[j]:
				Characteristics[i][j] = 1
	#print Characteristics


	for h in range(k):
		rp = random.permutation(len(Words))
		for j in range(len(S)):
			w = 0
			while Characteristics[rp[w]][j] != 1:
				w += 1
			Signatures[h][j] = w

	#print Signatures
	#print Words
	return Words, Signatures

#minhash([ [1, 2, 3], [3, 4, 5] ], 3)

#s = [['hoi'], ['hoi', 'doei'], ['oi', 'oei']] # 'S is a list of lists of strings'
S =  [ ['hoi'], ['hoe', 'gaat', 'het'], ['groet'] ]
w, s = minhash(S, 2)

print w
print s

#and returns two objects: a sorted list of all strings that occur in S
# Sorted how?
