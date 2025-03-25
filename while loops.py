evens = []
x = 0

while x <= 100:
	if x == 58:
		x+=1
		continue
	if x%2 == 0:
		evens.append(x)
	if x == 100:
		print(evens)
		break
	x += 1
print('\n',x)
