# Create a series of functions based on the below descriptions.

# Odd/Even:
# Create a function called odd_even that counts from 1 to 2000. 
# As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number.

# Multiply:
# Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) 
# and returns a list where each value has been multiplied by 5.

# --------------------------------------------------------

# def odd_even(start,end):
# 	for i in range (start,end+1):
# 		print "Number is ",i,". This is an ",
# 		if (i%2==1):
# 			print "odd number."
# 		else:
# 			print "even number."

# odd_even(1,2000)

# -----------------------------------------------

a = [2,4,10,16]

def multiply(a,b):
	newArray = []
	for i in range (len(a)):
		newArray.append(a[i]*b)
	return newArray

b = multiply(a,5)
print b