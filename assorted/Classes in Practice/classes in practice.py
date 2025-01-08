# create class with health and energy
class Monster:

	# attributes
	name = 'monster'
	health = 100
	energy = 50

	# methods
	def attack(self,amount):
		print(f'The {self.name} has attacked for {amount} points!')

	def move(self,distance):
		print(f'The {self.name} has moved {distance} spaces!')

# make a monster variable object by calling the Monster class
monster = Monster()
monster2 = Monster()
# printing health and energy values that are in the monster object
print(monster.health)
print(monster.energy)

monster.name = 'thug'
monster.attack(amount = monster.energy)

monster2.name = 'punk'
monster2.move(3)