# #problem in scope
def update_health(thing, amount):
	thing.health += amount

# health = 10

# print(health)
# update_health(20)
# print(health)

class Monster:
	def __init__(self, health, energy):
		self.health = health
		self.energy = energy
	def get_damage(self, amount):
		self.health -= amount

punk = Monster(100, 50)

# update_health(punk, 20)

# print(punk.health)

############################
##########Practice##########
############################

class Hero:
	def __init__(self, damage, monster):
		self.damage = damage
		self.monster = monster
	def attack(self):
		self.monster.get_damage(self.damage)


hero = Hero(30, punk)

print(vars(hero))
print(vars(punk))

hero.attack()

print(vars(punk))