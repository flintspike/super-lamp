my_list = [1,2,3,4,5,6,7,8]


def powers(num):
	return num ** 2

def lt4(num):
	if num < 4:
		return num

print(list(map(powers,my_list)))
print(list(map(lambda num: num**2,my_list)))
_list1 = [num ** 2 for num in my_list]
print(_list1)

print(list(filter(lambda num: num <5, my_list)))
_list2 =  [num for num in my_list if num < 5]
print(_list2)



