class Monster:
	health = 100
	energy = 100
	name = 'butt'
	def __init__(self, health, energy, name):
		self.health = health
		self.energy = energy
		self.name = name

	#methods
	def attack(self, target, amount):
		self.energy -= 10
		print(f'{self.name} attacked, leaving {self.energy} remaining.')
		target.hurt(amount)

	def hurt(self, amount):
		self.health -= amount
		print(f'{self.name} was hurt for {amount} damage!')
		print(f'{self.name} has {self.health} remaining.')

	def move(self, distance):
		print(f'{self.name} moved {distance} spaces.')

class Shark(Monster):
	def __init__(self, speed, name):
		super().__init__(health = 100,energy = 200, name = name)
		self.speed = speed
	def bite(self):
		print(f'{self.name} has bitten.')
	def move(self, distance):
		print(f'{self.name} swam {distance} spaces at a speed of {self.speed}.')

class Scorpion(Monster):

	poison_damage = 5

	def __init__(self, health, energy):
		super().__init__(health, energy,'Scorpy')

	def attack(self, target):
		self.energy -= 10
		target.hurt(self.poison_damage)
		print(f'{self.name} has attacked and induced {self.poison_damage} poison damage!')

# ACTIVE CREATURES
Shark = Shark(speed = 3, name ='Shark')
God = Monster(1000000,1000000, 'God')
Scorpion = Scorpion(40, 80)


Shark.attack(God, 10)

God.move(2)
Shark.move(1)
Scorpion.attack(God)
Scorpion.move(3)
print(Scorpion.health)