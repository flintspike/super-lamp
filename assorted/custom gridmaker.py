import fs
#makes a square of numbers

def int_check(num): #checks if input is an int and prompt again if it is not
	try: 
		num = int(num)
		return(num)
	except ValueError:
		print('Only use integers')
		return int_check(input('num: '))

x_clist = [num for num in range(0,int_check(input('X length: ')))] 
y_clist = [num for num in range(0,int_check(input('Y length: ')))]

for num in range(0,(len(x_clist)*len(y_clist))):
	if num % len(x_clist) == 0 and num != 0 :
		print('\n')

	if len(str(num)) < len(str(len(x_clist)*len(y_clist))):
		zeros = len(str(len(x_clist)*len(y_clist))) - len(str(num+1))
		for zero in range(zeros): print('0', end = '')
	print(num+1, end = ' ')