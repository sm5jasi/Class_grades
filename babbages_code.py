import math
def statistics(a):
	mean = math.sum(a) / len(a)
	std = math.std(a)
	high_score = max(a)
	low_score = min(a)
	return mean, std, high_score, low_score