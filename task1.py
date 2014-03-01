from sets import Set
def jsim(s1, s2):
	return float(len(Set(s1).intersection(Set(s2)))) / len(Set(s1).union(Set(s2)))

#print jsim(Set([1, 2, 3]), Set([2, 3, 4]))
