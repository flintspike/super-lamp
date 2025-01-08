# list1 = [4,6,2,8,1,7,9,5,3]

#list to be sorted:
list2 = [('a',3),('b',10),('c',6),('d',5)]

#the funtion that will be the key to be used by 'sorted' funtion
def sort_func(item):
	return item[1]
	

#do NOT call the sort func, only provide the name. The call will be handled intern
print(sorted(list2, key = sort_func))

#same as above but using a lambda instead of a func
print(sorted(list2, key = lambda item: item[1]))

inventory_names = ['Screws', 'Wheels', 'Metal parts', 'Rubber bits', 'Screwdrivers', 'Wood'] 
inventory_numbers = [43, 12, 95, 421, 23, 43]


####################
####################
####################


comb_list = list(zip(inventory_names,inventory_numbers))


#sort by number
numsort = sorted(comb_list, key = lambda item: item[1])
print(numsort)

#sort by len length
lensort = sorted(comb_list, key = lambda item: len(item[0]))
print(lensort)