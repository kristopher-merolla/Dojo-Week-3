# Assignment: Stars
# Write the following functions.

# Part I
# Create a function called draw_stars() that takes a list of numbers and prints out *.

# For example:
# x = [4, 6, 1]
# draw_stars(x)should print the following in when invoked:
# ****
# ******
# *

# Part II
# Modify the function above. Allow a list containing integers and strings to be passed to the draw_stars() function. When a string is passed, instead of displaying *, display the first letter of the string according to the example below. You may use the .lower() string method for this part.

# For example:

# x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

# draw_stars(x) should print the following in the terminal:

# ****
# ttt
# *
# mmmmmmm
# *****
# *******
# jjjjjjjjjjj

# ---------------------------------------------------------------

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def draw_stars(x):
	for i in range(0,len(x)):
		# print i,x[i],
		# print type(x[i]) is int
		if type(x[i]) is int:
			for j in range(x[i]):
				if (j == x[i]-1):
					print "*"
				else:
					print "*",
		else:
			for j in range(len(x[i])):
				if (j == len(x[i])-1):
					print x[i][0].lower()
				else:
					print x[i][0].lower(),

draw_stars(x)