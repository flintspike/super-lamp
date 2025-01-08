my_list = [1,2,3,4,5]

def filters(num):
	return num < 4


print(list(map(lambda num : num ** 2,my_list)))

print(list(filter(filters,my_list)))

print(list(filter(lambda num : num < 4,my_list)))

over4 = [num for num in my_list if num < 4]
powers = [num ** 2 for num in my_list]

print(powers)

print(over4)
