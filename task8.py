from numpy import random, empty, dot, allclose, arccos, histogram
from task4 import sketch
from datetime import datetime
from scipy import linalg

def cossim(s1, s2):
	hoi = dot(s1, s2) / dot(linalg.norm(s1),linalg.norm(s2))
	if allclose(hoi, 1): # Fix for problems with float64 and invalid math error
		ac = 0
	else:
		ac = arccos(hoi)
	return 1 - ac

rv = random.randn(1000, 2) # Random vectors
print 'rv done'

cs = empty((1000, 1000))
for i in range(1000):
    for j in range(0, i + 1):
        cs[i][j] = cossim(rv[i], rv[j])
        cs[j][i] = cs[i][j]
print 'cs done'

sketches = sketch(cs, 100)
print 'sketches done'

combinations = [(2, 50), (5, 20), (10, 10), (20, 5), (50, 2)] # All combinations of r and b
count = histogram(cs, bins=[0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85])[0] # Count the occurences of all interval probabilities
for b, r in [combinations[1]]:
    print '============='
    print b, r
    print datetime.now()
    detected = [0]*7
    for i in range(1000):
        print i # Shows some progress
        for j in range(1000): # For every random vector i and j
            # Check in which interval the jaccard similarity is
            countindex = 0
            if cs[i][j] >= 0.15 and cs[i][j] < 0.25:
                countindex = 0
            elif cs[i][j] >= 0.25 and cs[i][j] < 0.35:
                countindex = 1
            elif cs[i][j] >= 0.35 and cs[i][j] < 0.45:
                countindex = 2
            elif cs[i][j] >= 0.45 and cs[i][j] < 0.55:
                countindex = 3
            elif cs[i][j] >= 0.55 and cs[i][j] < 0.65:
                countindex = 4
            elif cs[i][j] >= 0.65 and cs[i][j] < 0.75:
                countindex = 5
            elif cs[i][j] >= 0.75 and cs[i][j] < 0.85:
                countindex = 6
            
            # Check if the two subsets will be detected as candidate pair with banding technique
            h = False
            bi = 0
            while h == False and bi < b:
                h = hash(tuple(sketches[range(bi * r, (bi + 1) * r)][:, i])) == hash(tuple(sketches[range(bi * r, (bi + 1) * r)][:, j]))
                bi += 1
            if h:
                detected[countindex] += 1
                
    print '============='
    print 'b=' + str(b) + '; r='+str(r)
    print 's=0.2; predicted=' + str(1-pow(1-pow(0.2, r), b)) + '; measured=' + str(detected[0]/float(count[0]))
    print 's=0.3; predicted=' + str(1-pow(1-pow(0.3, r), b)) + '; measured=' + str(detected[1]/float(count[1]))
    print 's=0.4; predicted=' + str(1-pow(1-pow(0.4, r), b)) + '; measured=' + str(detected[2]/float(count[2]))
    print 's=0.5; predicted=' + str(1-pow(1-pow(0.5, r), b)) + '; measured=' + str(detected[3]/float(count[3]))
    print 's=0.6; predicted=' + str(1-pow(1-pow(0.6, r), b)) + '; measured=' + str(detected[4]/float(count[4]))
    print 's=0.7; predicted=' + str(1-pow(1-pow(0.7, r), b)) + '; measured=' + str(detected[5]/float(count[5]))
    print 's=0.8; predicted=' + str(1-pow(1-pow(0.8, r), b)) + '; measured=' + str(detected[6]/float(count[6]))
    print datetime.now()
