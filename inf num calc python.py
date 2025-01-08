numbers = []

def get_num():
	num = input('give number or type y to add: ')
	if num == 'y': add(numbers)
	else:
		try: 
			num = int(num)
			numbers.append(num)
			print(numbers)
			get_num()
		except ValueError:
			print('Only use integers')
			end()

def end():
	ans = input('play again? y/n: ')
	if ans == 'y': get_num()
	elif ans == 'n': input('input to quit '); quit()
	end()

def add(arg):
	print(sum(arg))
	end() 

get_num()