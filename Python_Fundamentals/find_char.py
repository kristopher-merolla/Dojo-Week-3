# Write a program that takes a list of strings and a string containing a single character, and prints a new list of all the strings containing that character.

# Here's an example:

# # input
l = ['hello','world','my','name','is','Anna']
char = 'o'
n = []
# # output
# n = ['hello','world']

# ---------------------------------------------------
for i in range (0,len(l)):
	print l[i].find(char)
	if (l[i].find(char) == -1):
		continue
	else:
		n.append(l[i])
print n