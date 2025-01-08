class Monster:
	def __init__(self, health):
		self.health = health

	def get_damage(self, amount):
		self.health -= amount
		print(f'hurt for {amount} hp!')
		print(f'remaining health: {self.health}!')

	def attack(damage):
		print("Attacked with ")

class Hero(Monster):
	def __init__(self, damage, health):
		Monster.__init__(self, health)
		self.damage = damage
		self.type = type
	def attack(self,target):
		target.get_damage(self.damage)

class Scorpion(Monster):
	def __init__(self, poison_damage, scorpion_hp):
		super().__init__(scorpion_hp)
		self.poison_damage = poison_damage

	def attack(self):
		print("The Scorpion has attacked")
		print(f'It dealth {self.poison_damage} poison damage')

scorpy = Scorpion(15, 300)

scorpy.attack()
scorpy.get_damage(60)


