import numpy as np

def getFuzzyInput_anc(x):
	# rendah = 1; tinggi = 2
	
	nuLow = round(0,3)
	nuHi = round(0,3)

	# fuzzy set rendah
	lowA = round(0,3)
	lowB = round(2,3)

	# fuzzy set tinggi
	hiA = round(0,3)
	hiB = round(2,3)

	if (x > lowA) and (x < lowB):
		nuLow = round((lowB-x) / (lowB-lowA),3)
		nuHi = round((x - hiA) / (hiB - hiA),3)
		anc = np.array([[1, nuLow], [2, nuHi]])
	elif (x >= hiB):
		anc = np.array([[1, 0.001], [2, 0.999]])

	return anc
