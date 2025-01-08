# num_list = ['one','two','three','four','five','six','seven','eight','nine','ten']
# num_string = 'ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN'
# int_list = [1,2,3,4,5,6,7,8,9,10]
# split_string = num_string.split(' ')
# l2s = ' '.join(num_list)

# int_str = str(int_list)
# int_str = int_str[1:30]
# int_str = int_str.replace(',','')
# print(int_str)



# test_dict = {
# 'atk': 100 , 
# 'def':85 , 
# 'mag':30 , 
# 'hp':200,
# 'inv':['helm', 'sword', 'sheild']
# }
# print(test_dict['atk'])
# test_dict['atk'] += 10
# print(test_dict['atk'])

# shell_tuple = []
# test_set = {'cheese', 'cheese', 'hat', 'bowl',3,2,4}
# set_conv = tuple(test_set)
# print(set_conv[2])



# all_set = {'one','two','three','four','five','six','seven','eight','nine','ten'}
# odd_set = {'one','three','five','seven','nine'}
# evn_set = {'two','four','six','eight','ten'}

# print(odd_set.union(evn_set))
# print(odd_set | evn_set)
# print(all_set.intersection(odd_set))
# print(all_set & odd_set)
# print(all_set.difference(evn_set))
# print(all_set - evn_set)


# color = 'blue'

# match color:
# 	case 'red':
# 		print('red')
# 	case 'blue':
# 		print('blue')
# 	case 'green':
# 		print('green')
# 	case _:
# 		print('invalid')



# #even list generator
# evens = []
# count = 0
# while count <= 100:
# 	if count % 2 == 0 and count != 58:
# 			evens.append(count)
# 	count += 1
# print('')


# #odd list generator
# odds = []
# for dig in range(0,100,):
# 	if dig % 2 != 0 and count != 58:
# 		odds.append(dig)
# print(odds)


# practice = [[10,40,20,50], [2,42,10], [101,10,4]]

# for group in practice:
# 	for num in group:
# 		if num <= 50 and num > 10:
# 			print(num)


# #word combiner
# word_one = input('word one ')
# word_two = input('word two ')
# def mad_lib(one, two):
# 	print(str(one),'likes',str(two))
# mad_lib(word_one,word_two)
# input('press enter to exit')

# #calc
# def calc(num1, num2, operation):
# 	if operation == 'plus': print(num1 + num2)
# 	if operation == 'minus': print(num1 - num2)
# 	if operation == 'times' or operation == 'multiply' \
# 	or operation == 'multiplication': print(num1 * num2)

# def calc2(num1, num2, operation):
# 	match operation:
# 		case '-': print(num1 - num2)
# 		case '+': print(num1 + num2)
# 		case '*': print(num1 * num2)

# calc(5,5,'plus')
# print('++++')
# calc(20,10,'minus')
# print('++++')
# calc(2, 5, 'times')
# print('++++')
# print('++++')
# print('++++')
# calc2(20,10,'-')
# print('++++')
# calc2(5,5,'+')
# print('++++')
# calc2(2,5,'*')
# print('++++')

# #greeting practice

# def greeting(greeting, name = 'sir', day = 'day'):
# 	print(f'{greeting}, {name}. Lovely {day} we are having.')
# greeting('Hello',name = 'James',day = 'Tuesday')
