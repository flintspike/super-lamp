class Monster:
	def __init__(self, health, energy,):
		self.health = health
		self.energy = energy

	# def attack(self, amount):
	# 	print("The monster attacks!")
	# 	print(f'{amount} damage was dealt!')

	# def move(self, distance):
	# 	print('The monster has moved.')
	# 	print(f'{distance} spaces were traveled.')

class Fish:
	def __init__(self, speed, has_scales, **kwargs):
		self.speed = speed
		self.has_scales = has_scales
		super().__init__(**kwargs)

	# def swim(self):
	# 	print(f'The Fish has moved at a speed of {self.speed}')

class Shark(Fish, Monster):
	def __init__(self, bite_strength, speed, has_scales, health, energy):
		self.bite_strength = bite_strength
		super().__init__(speed = 400, has_scales = True, health = 1000, energy = 300)

pekneed = Shark(bite_strength = 200, speed = 400, has_scales = True, health = 1000, energy = 300)

print(pekneed.health)
print(pekneed.energy)
print(pekneed.speed)
print(pekneed.has_scales)