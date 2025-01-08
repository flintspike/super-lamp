def add(a,b):
	return a + b

class Test:
	def __init__(self, add_func):
		self.new_func = add_func

test = Test(add_func = add)


#print(dir(test))

#######################
####################### practice
#######################

class Monster:
	def __init__(self, func):
		self.func = func

class Attacks:
		def attack1(self):
			print('attack 1')
		def attack2(self):
			print('attack 2')
		def attack3(self):
			print('attack 3')
		def attack4(self):
			print('attack 4')

bat = Monster(Attacks().attack1)

bat.func()

