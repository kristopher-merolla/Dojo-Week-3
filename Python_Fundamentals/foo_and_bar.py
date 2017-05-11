# Optional Assignment: Foo and Bar
# Write a program that prints all the prime numbers and all the perfect squares for all numbers between 100 and 100000.

# For all numbers between 100 and 100000 test that number for whether it is prime or a perfect square. If it is a prime number print "Foo". If it is a perfect square print "Bar". If it is neither print "FooBar". Do not use the python math library for this exercise. For example, if the number you are evaluating is 25, you will have to figure out if it is a perfect square. It is, so print "Bar".

# This assignment is extra challenging! Try pair programming and pulling up a white board.

# ----------------------------------------------

# The function fooBar will print "Foo" on prime numbers, "Bar" on perfect squares, and "FooBar" if the number is neither
def fooBar(a,b):
	prime_list = []
	perfect_square_list = []
	c = int(b**(0.5))+1
	for i in range (a,b+1):
		if (i == 1):
			perfect_square_list.append(i)
			print "Bar",i #found as perfect square
		elif (i == 5 or i == 2 or i == 3):
			prime_list.append(i)
			print "Foo",i #found as prime
		elif (i%2 == 0 or i%3 == 0 or i%5 == 0):
			# print "Not Prime"
			temp = 0
			for j in range (a,c):
				if (j**2==i):
					print "Bar",i #found as perfect square
					perfect_square_list.append(i)
					temp += 1
					break
				elif (temp==1):
					continue
			if (temp==0):
				print "FooBar",i #not a prime or perfect square
		else:
			prime_list.append(i)
			print "Foo",i #found as prime
	print prime_list
	print perfect_square_list

#The function findPrime will find the prime numbers
def findPrime(a,b):
	prime_list = []
	for i in range (a,b+1):
		if (i == 1):
			continue
		elif (i == 5 or i == 2 or i == 3):
			prime_list.append(i)
			print "Prime"
		elif (i%2 == 0 or i%3 == 0 or i%5 == 0):
			continue
		else:
			prime_list.append(i)
			print "Prime"
	return prime_list

#The function findPerfectSquare will find the perfect squares
def findPerfectSquare(a,b):
	c = int(b**(0.5))+1
	perfect_square_list = []
	for i in range (a,b+1):
		for j in range (a,c):
			if (j**2==i):
				print "Perfect Square"
				perfect_square_list.append(i)
			else:
				continue
	return perfect_square_list


# Function calls must be after the function definition

# fooBar(100,100000)

fooBar(1,100)

# print int(100**(0.5))

# print findPrime(1,70)

# print findPerfectSquare(1,100)




