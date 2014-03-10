from numpy import dot, pi, arccos, allclose
from math import sqrt, acos, pi

def cossim(s1, s2):
	#return  1 - acos(dot(s1, s2) / (sqrt(dot(s1, s1)) * sqrt(dot(s2, s2)))) / pi
	hoi = dot(s1, s2) / dot(linalg.norm(s1),linalg.norm(s2))
	if allclose(hoi, 1):
		ac = 0
	else:
		ac = arccos(hoi)
	return 1 - ac


	
#print cossim([1, 2, 3], [3, 4, 5])
#print cossim([1, 2, 3], [1, 2, 3])
