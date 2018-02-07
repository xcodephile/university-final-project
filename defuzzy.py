def defuzzy(a, b, c, d):
	
	temp = ((a*10)+(b*300)+(c*900)+(d*3600)/(a+b+c+d))
	return round(temp,3)
