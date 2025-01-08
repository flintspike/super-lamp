class Parent_3 :
	def __init__(self, arg3, arg4):
		self.attribute_3 = arg3
		super().__init__(**kwargs)

class Parent_4 :
	def __init__(self, arg4, arg5):
		self.attribute_4 = arg4
		super().__init__(**kwargs)

class Parent_5 :
	def __init__(self, arg5):
		self.attribute_5= arg5

class Parent_1(Parent_3):
	def __init__(self, arg1, arg3, **kwargs):
		print(kwargs)
		self.attribute_1 = arg1
		print(kwargs)
		super().__init__(**kwargs)

class Parent_2(Parent_3, Parent_4) :
	def __init__(self, arg2, arg3, arg4, **kwargs):
		print(kwargs)
		self.attribute_2 = arg2
		print(kwargs)
		super().__init__(**kwargs)

class six(Parent_1,Parent_2,Parent_5):
	def __init__(self,**kwargs):
		print(kwargs)
		super().__init__(**kwargs)

sixer = six(arg1 = 1, arg2 = 2, arg3 = 3, arg4 = 4, arg5 = 5)
print(vars(sixer))

