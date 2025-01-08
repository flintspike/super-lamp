# create class with health and energy
class Monster:

	# attributes
	name = 'monster'
	health = 100
	energy = 50
	stranth = 15

	def __str__(self): #is called when the created object (i.e. monster1) gets put into a 'str()' call
		return f'You see a {self.name} with {self.health} health and {self.energy} energy'

	def __init__(self, name): #is called upon object creation (class assignment)
		self.name = name
		print(f'A {self.name} has appeared!')

	def attack(self, amount):
		print(f'The {self.name} has attacked for {self.stranth} damage!')
		self.energy -= 10
		print(f'The {self.name} has {self.energy} energy remaining.')

	def move(self, distance):
		print(f'The {self.name} has moved {distance} spaces.')

enemy1 = Monster('Bum')
enemy2 = Monster('Thug')

enemy1.attack(20)
enemy1.move(2)

enemy2.attack(10)
enemy2.attack(10)
enemy2.move(3)

print(enemy1.energy)
print(enemy2.energy)

#putting the object into a str() call, calls the __str__() method inside of the monster object
print(str(enemy2))
#doens't actually even require str() to be called, as the str() command looks for a string as-is
print(enemy1)