inventory_names = ['screws', 'wheels', 'metal parts', 'rubber bits', 'screwdrivers', 'wood']
inventory_numbers = [43, 12, 95, 421, 23, 43]

inv = list(zip(inventory_names,inventory_numbers))

# for index, name in enumerate(inv):
# 	print(f'{index}: {name}')

# my_list = [num for num in range(0,100)]
# for num in my_list: print(num)
# print(inventory_numbers)

# print([(item, quant) for item, quant in inv if quant < 50])

# com_comp = [[x for x in range(5)] for y in range(5)]
# for row in com_comp:print(row)

cols = 'ABCDEFGH'
rows = list(range(1,9))

grid = [[f'{x}{y}' for y in rows] for x in cols[::-1]]

for row in grid: print(row)
