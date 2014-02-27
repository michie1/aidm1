from sets import Set
def jsim(s1, s2):
	return float(len(s1.intersection(s2))) / len(s1.union(s2))

#print jsim(Set([1, 2, 3]), Set([2, 3, 4]))
