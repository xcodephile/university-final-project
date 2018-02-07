import numpy as np
from defuzzy import defuzzy

def inference(fuzzyInput):
	# Ket. input rules: 1=Low; 2=Middle; 3=High
	# Ket. output rules: 1=Low ; 2=Middle ; 3=High


	# RULES ===============================================================================
	rules = np.array([[0,1,0],[1,1,1], [2,1,1], [3,1,2], [0,2,3], [1,2,3], [2,2,2], [3,2,2]])


	# KOMBINASI FUZZY SET ANTAR FK ========================================================
	# temp = matriks 4x4
	temp = np.zeros(shape=(4,4))
	
	temp[0,0] = fuzzyInput[0,0]
	temp[0,1] = fuzzyInput[0,1]
	temp[0,2] = fuzzyInput[0,2]
	temp[0,3] = fuzzyInput[0,3]

	temp[1,0] = fuzzyInput[0,0]
	temp[1,1] = fuzzyInput[0,1]
	temp[1,2] = fuzzyInput[1,2]
	temp[1,3] = fuzzyInput[1,3]

	temp[2,0] = fuzzyInput[1,0]
	temp[2,1] = fuzzyInput[1,1]
	temp[2,2] = fuzzyInput[0,2]
	temp[2,3] = fuzzyInput[0,3]

	temp[3,0] = fuzzyInput[1,0]
	temp[3,1] = fuzzyInput[1,1]
	temp[3,2] = fuzzyInput[1,2]
	temp[3,3] = fuzzyInput[1,3]


	# PENCOCOKAN RULES ====================================================================
	# temp2 = matriks 4x1 untuk menampung fuzzy output
	temp2 = np.zeros(shape=(4,1))
	for i in range(0,4):
		for j in range(0,8):
			if (temp[i][0] == rules[j][0]):
				if (temp[i][2] == rules[j][1]):
					temp2[i][0] = rules[j][2]
					break


	# AND [KONJUNGSI. MENCARI NILAI TERENDAH] =============================================
	# temp3 = matriks 8x1 untuk menampung dk output
	temp3 = np.zeros(shape=(4,1))
	for i in range(0,4):
		A = np.array([temp[i][1], temp[i][3]])
		temp3[i][0] = A[A>0].min()
		if (temp3.size == 0):
			temp3[i][0] = 0


	# OR [DISJUNGSI PART 1: MENCARI HIMPUNAN YANG SAMA] ===================================
	nIsEmpty = 1	
	lIsEmpty = 1
	mIsEmpty = 1
	hIsEmpty = 1
	temp4a = np.zeros(shape=(4,1))
	temp4b = np.zeros(shape=(4,1))
	temp4c = np.zeros(shape=(4,1))
	temp4d = np.zeros(shape=(4,1))
	for i in range(0,4):
		if (temp3[i][0] <> 0):
			if (temp2[i][0] == 0):
				temp4a[i][0] = temp3[i][0]
				nIsEmpty = 0
			elif (temp2[i][0] == 1):
				temp4b[i][0] = temp3[i][0]
				lIsEmpty = 0
			elif (temp2[i][0] == 2):
				temp4c[i][0] = temp3[i][0]
				mIsEmpty = 0
			elif (temp2[i][0] == 3):
				temp4d[i][0] = temp3[i][0]
				hIsEmpty = 0
			else:
				continue


	# OR [DISJUNGSI PART 2: MENCARI NILAI TERTINGGI TIAP HIMPUNAN] =========================
	if (nIsEmpty == 1):
		temp4aOut = 0 #temp4aOut = nilai tertinggi dari himpunan low
	else:
		temp4aOut = temp4a.max()	
	if (lIsEmpty == 1):
		temp4bOut = 0
	else:
		temp4bOut = temp4b.max()
	if (mIsEmpty == 1):
		temp4cOut = 0
	else:
		temp4cOut = temp4c.max()
	if (hIsEmpty == 1):
		temp4dOut = 0
	else:
		temp4dOut = temp4d.max()


	# HITUNG CRISP VALUE ====================================================================
	crispValue = defuzzy(temp4aOut, temp4bOut, temp4cOut, temp4dOut)

	return crispValue
