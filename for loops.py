practice_list = [[10,40,20,50], [2,42,10], [101,10,4]]

for group in practice_list:
	for num in group:
		if num >= 100:
			break
		if num > 10 and num < 50:
			print(num)
