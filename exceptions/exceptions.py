import fs

#standard all inclusive try/except
try:
	print(1/0)
except:
	print('section 1: standard try/except: cant do that \n')


#error specific try/except (only first error will trigger, below errors will be skipped)
try:
	print('Try')
	# print(null_var)
	# print(1/0)

except ZeroDivisionError:
	print('Cannot divide by zero.')
except NameError:
	print("Var doen't exist")
else:
	print('Else triggered')
finally:
	print('This will print with or without errors')

#raisning exceptions (custom errors)

# var_must_be_string = 'strictly string',4
# if isinstance(var_must_be_string,str):
# 	print(var_must_be_string)
# else:
# 	raise TypeError('not a string')

#################################
############PRACTICE#############
#################################

list_a = ['apple','burger','cranberry','donuts','eggs','fries','grapes']
try:
	print(list_a['a'])
except IndexError:
	print('The index does not exist, so the \"IndexError\" will run,')
except:
	print('\"except\" is a non-specific failstate error and will run when another error type condition is not met.')
else:
	print('\"else\" happens in success')
finally:
	print('as will \"finally\"')