lets = 'ABCDE'

#creates a dictionary with a value that increases based on num:lets within the predetermined range
dic = {num:lets[num-1] for num in range(1,6)}
for item in dic: print(item,dic[item],'\n')