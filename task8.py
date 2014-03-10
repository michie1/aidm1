from numpy import random, empty, dot, pi
from math import acos, sqrt
from scipy import linalg
def cossim(s1, s2):
    """return  1 -\
        acos(dot(s1, s2) /\
         (sqrt(dot(s1, s1)) *\
             sqrt(\
                dot(s2, s2)\
            ))) /\
                pi"""
    return  1 - \
				acos(dot(s1, s2) /\
					(dot(\
							linalg.norm(s1),\ # Prima
							linalg.norm(s2)	# math domain error
						)
					)
				) /\
				pi    
a = [-0.27168949, -2.44429191]
print cossim(a, a)
