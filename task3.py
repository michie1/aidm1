from scipy import spatial
from numpy import dot
from math import sqrt, acos, pi


def cossim(s1, s2):
	return  1 - acos(dot(s1, s2) / (sqrt(dot(s1, s1)) * sqrt(dot(s2, s2)))) / pi
	
print cossim([1, 2, 3], [3, 4, 5])
print cossim([1, 2, 3], [1, 2, 3])
