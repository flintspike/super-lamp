chess = [[f'{let}{num}' for num in range(1,9)] for let in 'ABCDEFGH'[::-1]]
for row in chess:
	print(row)