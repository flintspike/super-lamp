# def procalc(num1, num2, operation):
# 	if operation == 'plus':
# 		print(float(num1) + float(num2))
# 	if operation == 'minus':
# 		print(float(num1) - float(num2))

# procalc(input('enter num1: '),input('enter num2: '), input('plus or minus: '))

def greeter(
	weekday,
	person = 'Man',
	greet = 'hello'
	):

	print(f'{greet.capitalize()} {person.capitalize()}! Happy {weekday}.')

greeter('Monday',greet = 'wattup', person = 'Fred')