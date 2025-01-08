a = 1
del a

a = [1,2,3,3]

# del item by index
del a[1]
print(a)

# remove by value
a.remove(3)
print(a)

# pop (this also returns the value that has been removed!)
print('removed ', a.pop(-1))
print(a)

#clear entire list
a.clear()
print(a)