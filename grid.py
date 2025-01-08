my_clist = [num for num in range(0,int(input('max cels: ')))]
max_width = int(input('max width: '))
for num in my_clist:
	if num % max_width == 0:
		print('\n')
	for char in len(str(my_clist[-1])):
		if len(str(num)) < char: print('0', end = '')
	print(num, end = ' ')
input('\ninput to exit')