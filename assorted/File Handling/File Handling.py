# # old manual way
# file = open('test.txt') #this loads the file into memory in a variable called 'file'
# print(list(file)) #this prints the file as a list
# file.close() #this closes the file and removes it from memory

# new way using 'with' operator
with open('test.txt') as file:  #this opes the file as 'file' and delegates the indented text as the actions to occur with this condition
	print(file.read()) #this prints the file as a list
	# for line in list(file): print(line) #this reads the file line by line
	# once the indented segment ends, the file is close and no longer stored in memory

with open('tree.txt','w') as file:
	file.write('''     / \\
    /   \\
   /     \\
  /       \\
 /_____\\
      ||
 ___||___''')