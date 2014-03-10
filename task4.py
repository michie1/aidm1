from numpy import zeros, random, dot, array

def sketch(M, k):
	rd = random.randn(k, len(M))
	sketches = zeros((k, len(M[0])))
	for i in range(k):
		for j in range(len(M[0])):
			v = dot(rd[i], M[:, j])
			if v > 0:
				sketches[i][j] = 1
			elif v < 0:
				sketches[i][j] = -1
			else:
				if random.random() >= 0.5:
					sketches[i][j] = 1
				else:
					sketches[i][j] = -1
	return sketches

#sketch(array([[1.0, 2.0, 3.0], [1.0, 2.0, 3.0]]), 2)
