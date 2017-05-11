# Assignment: MathDojo
# HINT: To do this exercise, you will probably have to use 'return self'. If the method returns itself (an instance of itself), we can chain methods.

# PART I
# Create a Python class called MathDojo that has the methods add and subtract. Have these 2 functions take at least 1 parameter.

# Then create a new instance called md. It should be able to do the following task:

# MathDojo().add(2).add(2, 5).subtract(3, 2).result

# which should perform 0+2+(2+5)-(3+2) and return 4.

# PART II
# Modify MathDojo to take at least one integer(s) and/or list(s) as a parameter with any number of values passed into the list. It should now be able to perform the following tasks:

# MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result

# should do 0+1+3+4+(3+5+7+8)+(2+4.3+1.25)-2-(2+3)-(1.1+2.3) and return its result.

# PART III
# Make any needed changes in MathDojo in order to support tuples of values in addition to lists and singletons.

# ------------------------------------------------------------

class MathDojo(object):
	def __init__(self):
		print "MathDojo Created"
		self.count = 0

	def add_num(self,a,b=0,c=0): #add_num can take as many as 3 inputs or as few as 1 input
		self.input1 = 0
		self.input2 = 0
		self.input3 = 0
		if (type(a) == int):
			self.input1 = a
		else:
			for i in range (len(a)):
				self.input1 += a[i]
		if (type(b) == int):
			self.input2 = b
		else:	
			for i in range (len(b)):
				self.input2 += b[i]
		if (type(c) == int):
			self.input3 = c
		else:
			for i in range (len(c)):
				self.input3 += c[i]
		self.count += self.input1+self.input2+self.input3
		return self

	def subtract_num(self,a,b=0,c=0):
		self.input1 = 0
		self.input2 = 0
		self.input3 = 0
		if (type(a) == int):
			self.input1 = a
		else:
			for i in range (len(a)):
				self.input1 += a[i]
		if (type(b) == int):
			self.input2 = b
		else:	
			for i in range (len(b)):
				self.input2 += b[i]
		if (type(c) == int):
			self.input3 = c
		else:
			for i in range (len(c)):
				self.input3 += c[i]
		self.count -= self.input1+self.input2+self.input3
		return self
		
	def result(self):
		return self.count

# md = MathDojo()
# print md.add_num(2).add_num(2,5).subtract_num(3,2).result()

md2 = MathDojo()
# print md2.add_num([1],3,4).add_num([3, 5, 7, 8], [2, 4.3, 1.25]).subtract_num(2, [2,3], [1.1, 2.3]).result()

tup1 = (1,1)
print md2.add_num(tup1,3,4).result()
# print md2.add_num([3, 5, 7, 8], [2, 4.3, 1.25]).result()