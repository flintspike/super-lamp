multi = 10
has_calced = False

def multiplier(num):
	global has_calced
	has_calced = True
	result = num * multi
	return result

print(multiplier(10))