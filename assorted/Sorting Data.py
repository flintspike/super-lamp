# list1 = [4,7,12,3,6,8,6,4,31,7,89,1,3,7,2,5]
# # print(sorted(list1, reverse = True))

# list2 = [
#     ('a', 12),
#     ('b', 35),
#     ('c', 78),
#     ('d', 4),
#     ('e', 90),
#     ('f', 123),
#     ('g', 56),
#     ('h', 8)
# ]

# def sort(item):
# 	return item[1]

# # print(sorted(list2, key = sort))

# print(sorted(list2, key = lambda item: item[0]))

# exercise 
inventory_names = ['Screws', 'Wheels', 'Metal parts', 'Rubber bits', 'Screwdrivers', 'Wood']
inventory_numbers = [43, 12, 95, 421, 23, 43]
combined_list = list(zip(inventory_names,inventory_numbers))

print(sorted(combined_list, key = lambda item: item[1])) #sort by inventory number
print(sorted(combined_list, key = lambda item: len(item[0]))) #sort by item name length