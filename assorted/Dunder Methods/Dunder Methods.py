# create class with health and energy
class Monster:

	# attributes
	name = 'monster'
	health = 100
	energy = 50
	stranth = 15

	def __init__(self, name):
		self.name = name
		print(f'A {self.name} has appeared!')

	def attack(self, amount):
		print(f'The {self.name} has attacked for {self.stranth} damage!')
		self.energy -= 10
		print(f'The {self.name} has {self.energy} energy remaining.')

	def move(self, distance):
		print(f'The {self.name} has moved {distance} spaces.')

enemy1 = Monster('Bum')

enemy1.attack(20)
enemy1.move(2)