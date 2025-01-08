string = 'test'
types = ['upper','title','lower','casefold']
for type in types:
	eval(f'print(string.{type}())')