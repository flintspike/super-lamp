##########
#practice#
##########



class Parent_3 :
	def __init__(self, arg):
		self.attribute_3 = arg

class Parent_4 :
	def __init__(self, arg):
		self.attribute_4 = arg

class Parent_5 :
	def __init__(self, arg):
		self.attribute_5= arg

class Parent_1(Parent_3):
	def __init__(self, arg1, arg3):
		Parent_3.__init__(self,arg3)
		self.attribute_1 = arg1

class Parent_2(Parent_3, Parent_4) :
	def __init__(self, arg2, arg3, arg4):
		Parent_3.__init__(self,arg3)
		Parent_4.__init__(self,arg4)
		self.attribute_2 = arg2

class six(Parent_1,Parent_2,Parent_5):
	def __init__(self, arg1, arg2, arg3, arg4, arg5):
		Parent_1.__init__(self,arg1,arg3)
		Parent_2.__init__(self,arg2,arg3,arg4)
		Parent_5.__init__(self,arg5)

sixer = six(1,2,3,4,5)

# print(sorted(vars(sixer)))

##########
#practice#
##########

