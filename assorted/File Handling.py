# #open and close manually
# file = open('File Handling.txt')
# print(list(file))
# s = input('step')
# file.close()


# #open and close manually
# with open('File Handling.txt') as file:
# 	print(file.read())

with open('tree.txt','w') as file:
	file.write(
'''    /\\
   /  \\
  /    \\
 /______\\
    ||  
    ||''')