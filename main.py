import numpy as np
from getFuzzyInput_frk import getFuzzyInput_frk
from getFuzzyInput_anc import getFuzzyInput_anc
from inference import inference

def doFuzzy(x_frk,x_anc):
	
	# satuan dalam detik
	x_frk = int(x_frk)	

	# array_fuzzyInput = matriks 2x4
	array_fuzzyInput = np.zeros(shape=(2,4))
	array_frk = np.array([getFuzzyInput_frk(x_frk)])
	array_anc = np.array([getFuzzyInput_anc(x_anc)])

	array_fuzzyInput[0,0] = array_frk[0][0][0]
	array_fuzzyInput[0,1] = array_frk[0][0][1]
	array_fuzzyInput[0,2] = array_anc[0][0][0]
	array_fuzzyInput[0,3] = array_anc[0][0][1]
	array_fuzzyInput[1,0] = array_frk[0][1][0]
	array_fuzzyInput[1,1] = array_frk[0][1][1]
	array_fuzzyInput[1,2] = array_anc[0][1][0]
	array_fuzzyInput[1,3] = array_anc[0][1][1]

	crispValue = inference(array_fuzzyInput)

	# satuan dalam detik
	print int(round(crispValue))
