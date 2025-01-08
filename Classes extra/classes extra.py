class Monster:
	'''a standard monster class'''
	def __init__(self, health, energy):
		self.health = health
		self.energy = energy

		self._id = 5 #underscore just means you it is meant to be static. Do not change it. This is convention, not syntax.

	def attack(self, amount):
		print(f'The monster has attacked for {amount} damage!')
		self.energy -= 20

	def move(self, distance):
		print(f'The monster has moved {distance}.')

monster = Monster(100,100)

print(hasattr(monster, 'health')) # provides a True/False answer to if an object has a certain attribute.

setattr(monster, 'weapon', 'sword') # setattr adds an attribute to an object, in this case adding an attribute 'weapon' with the value 'sword'
print(monster.weapon)

print(monster.__doc__)