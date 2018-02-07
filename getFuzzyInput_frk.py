import numpy as np

def getFuzzyInput_frk(x):
	# sering = 1; sedang = 2; jarang = 3; satuan: detik
	
	nuNa = round(0,3)	
	nuLow = round(0,3)
	nuMid = round(0,3)
	nuHi = round(0,3)

	# fuzzy set sangat sering
	naB = round(0,3)
	naC = round(6,3)

	# fuzzy set sering
	lowA = round(0,3)
	lowB = round(6,3)
	lowC = round(360,3)

	# fuzzy set sedang
	midA = round(6,3)
	midB = round(360,3)
	midC = round(540,3)

	# fuzzy set jarang
	hiA = round(360,3)
	hiB = round(540,3)

	if (x == naB):
		frk = np.array([[0, 0.999], [1, 0.001]])
	elif (x > lowA) and (x < lowB):
		nuNa = round((naC - x) / (naC - naB),3)
		nuLow = round((x - lowA) / (lowB - lowA),3)
		frk = np.array([[0, nuNa], [1, nuLow]])
	elif (x == lowB):
		frk = np.array([[0, 0.001], [1, 0.999]])
	elif (x > midA) and (x < midB):
		nuLow = round((lowC - x) / (lowC - lowB),3)
		nuMid = round((x - midA) / (midB - midA),3)
		frk = np.array([[1, nuLow], [2, nuMid]])
	elif (x == midB):
		frk = np.array([[1, 0.001], [2, 0.999]])
	elif (x > midB) and (x < midC):
		nuMid = round((midC - x) / (midC - midB),3)
		nuHi = round((x - hiA) / (hiB - hiA),3)
		frk = np.array([[2, nuMid], [3, nuHi]])
	elif (x >= hiB):
		frk = np.array([[2, 0.001], [3, 0.999]])

	return frk
