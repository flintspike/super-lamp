item_names = ['sord', 'club', 'dagger', 'flail', 'torch', 'mace']
item_stats = [10, 20, 30, 40, 50, 60]

#prints the list in in format of [index] item - stat
#for item, stat in zip(enumerate(item_names),item_stats): print(f'[{item[0]}] {item[1].title()} - atk: {stat}')

#same as above script but is more retrievable and also includes a halfway point statement which can help to illustrate the retrieval process

data = enumerate(zip(item_names,item_stats))
for index in data: 
	print(f'[{index[0]}] "{index[1][0]}" - {index[1][1]}')
	if index[0] + 1 == len(item_names) // 2: print('half')