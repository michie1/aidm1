from task2 import minhash
from task1 import jsim

def sigsim(ss1, ss2, k = 2):
	#k = 1
	w, signatures = minhash([ss1, ss2], k)
	match = 0
	nomatch = 0
	for i in range(k):
		if signatures[i][0] == signatures[i][1]:
			match += 1
		else:
			nomatch += 1

	#return round(match / float(match + nomatch), 0)
	return match / float(match + nomatch)

#sa = ['a', 'b', 'c']
#sb = ['c', 'd', 'e']
#sa = [2]
#sb = [2]
#sa = ['a', 'b', 'c']
#sb = ['c', 'd', 'e']
#print 'sigsim', sigsim(sa, sb, k=100000)
#print 'jsim', jsim(sa, sb)
