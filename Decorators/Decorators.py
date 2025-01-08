import fs

#basic explanation
def HIDE():
	def cheese():
		print('function')

	def wrapper(func):
		print('yo')
		func()
		print('end')

	wrapper(cheese)

	#create a new function within a main function
	def func_gen():
		def new_func():
			print('new function')
		#return that funtion to the called instance
		return new_func
	#the function is assigned to a variable that called the parent function, 
	#the variable holds a funtion which then makes the variable become a func itself
	new_func = func_gen()
	#the varaible is now callable as a function
	new_func()

	print('############################################################\n \n \n.')
#multiple decorators in order of operation
def HIDE():
	def deco(function):
		def wrapper():
			print('deco begin')
			function()
			print('deco ends')
		return wrapper

	def duration_deco(func):
		def wrapper():
			start_time = time.time()
			func()
			time.sleep(2)
			duration = time.time() - start_time
			print(duration)
		return wrapper

	def double_up(func):
		def wrapper():
			func()
			func()
		return wrapper

	@double_up
	@duration_deco
	@deco
	def func():
		print('function')

	func()


def arg_deco(function):
	def wrapper(*args,**kwargs):
		print('passed')
		function(*args, *kwargs)
	return wrapper

@arg_deco
def printerfunc(ptext):
	print(ptext)

printerfunc('hello')