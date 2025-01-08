import random 
from datetime import datetime as dt

# The name of the modules will be written before the name of the actual function

random_numer = random.randint(0,9999)
print(random_numer)

Alphabet = {
 0: '###',
 1: 'apple',
 2: 'banana',
 3: 'cat',
 4: 'dog',
 5: 'elephant',
 6: 'fish',
 7: 'giraffe',
 8: 'hat',
 9: 'ice',
 10: 'jelly',
 11: 'kite',
 12: 'lion',
 13: 'monkey',
 14: 'nest',
 15: 'orange',
 16: 'pencil',
 17: 'quark',
 18: 'rabbit',
 19: 'snake',
 20: 'tiger',
 21: 'umbrella',
 22: 'violin',
 23: 'whale',
 24: 'xenon',
 25: 'yacht',
 26: 'zucchini'
}
print(random.choice(Alphabet))

print(dt.now())