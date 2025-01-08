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
	def __init__(self, speed):
		Monster.__init__(self,health = 100,energy = 200,name = 'Shark')
		self.speed = speed
	def bite(self):
		print(f'{self.name} has bitten.')
	def move(self, distance):
		print(f'{self.name} swam {distance} spaces at a speed of {self.speed}.')

Shark = Shark(speed = 3)

God = Monster(1000000,1000000, 'God')

Shark.attack(God, 10)

God.move(2)
Shark.move(1)