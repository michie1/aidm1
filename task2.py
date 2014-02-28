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

	rp = random.permutation(len(Words))
	print rp[0]
	print len(Words)
	print Characteristics[rp[4]][0]
	j = 0
	#while Characteristics[rp[j]][0] != 1:
	#	j += 1
	#Signatures[0][j] = 1

	print Signatures

#minhash([ [1, 2, 3], [3, 4, 5] ], 3)

#s = [['hoi'], ['hoi', 'doei'], ['oi', 'oei']] # 'S is a list of lists of strings'
S =  [ ['hoi'], ['hoe', 'gaat', 'het'], ['groet'] ]
minhash(S, 2)

#and returns two objects: a sorted list of all strings that occur in S
# Sorted how?
