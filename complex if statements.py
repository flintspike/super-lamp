# num = 21
# if num > 50 and num < 100 or num == 151:
# 	print('yipee fortnite und cola')

# money = 100
# hungry = True
# bored = False

# if money > 80 and hungry or bored:
# 	print('obey')

exlist = ['a','b','c']

if 'a' in exlist:
	print('a is in list')
	if 'b' in exlist:
		print('so is b')
	if 'c' in exlist:
		print('so is c')

if 'b' in exlist and 'a' not in exlist:
	print('b is in list')
	if 'c' in exlist:
		print('so is c')

if 'c' in exlist and 'a' not in exlist and 'b' not in exlist:
	print('c is in list')