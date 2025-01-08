#makes a square of numbers

def int_check(num):
	try: 
		num = int(num)
	except ValueError:
		print('Only use integers')
		int_check(input('num: '))
	return(num)

x_clist = [num for num in range(0,int_check(input('X length: ')))]
y_clist = [num for num in range(0,int_check(input('Y length: ')))]
for num in range(0,(len(x_clist)*len(y_clist))):
	if num % len(x_clist) == 0 and num != 0 :
		print('\n')
	if len(str(num)) < 2: print('0', end = '')
	print(num, end = ' ')