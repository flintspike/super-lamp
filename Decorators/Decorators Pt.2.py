import fs

def repeatwrap(kazu):	
	def deco(func):
		def wrapper():
			for r in range(kazu):
				func()
		return wrapper
	return deco	

@repeatwrap(100)
def typist():
	print('function')

typist()