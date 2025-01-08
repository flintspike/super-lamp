# alpha_list = ['a','b','c','d','e','f','g']
# num_list = [1,2,3,4,5,6,7,8]

# set_comp = {num for num in range(45)}

# dict_comp = {num:alph for (num,alph) in zip(num_list, alpha_list)}

# tuple_comp = tuple(num for num in range(45))

# print(set_comp)
# print(dict_comp)
# print(tuple_comp)

keys = [let for let in str('ABCDEFGH')]
vals = {num for num in range(8)}

my_dict = {key:vals for key in keys}

for key, val in my_dict.items(): print(key, val) 