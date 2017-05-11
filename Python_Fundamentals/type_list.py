# Write a program that takes a list and prints a message for each element in the list, based on that element's data type.

# Your program input will always be a list. For each item in the list, test its data type. If the item is a string, concatenate it onto a new string. If it is a number, add it to a running sum. At the end of your program print the string, the number and an analysis of what the array contains. If it contains only one type, print that type, otherwise, print 'mixed'.

# Here are a couple of test cases (l,m,n below)

# #input
l = ['magical unicorns',19,'hello',98.98,'world']
# #output
# "The array you entered is of mixed type"
# "String: magical unicorns hello world"
# "Sum: 117.98"

# # input
m = [2,3,1,7,4,12]
# #output
# "The array you entered is of integer type"
# "Sum: 29"

# # input
n = ['magical','unicorns']
# #output
# "The array you entered is of string type"
# "String: magical unicorns"

# -------------------------------------------------
k = l
mySum = 0
myStr = ""
for i in range (0,len(k)):
	if (type(k[i]) is str):
		myStr += k[i]
		myStr += " "
	elif (type(k[i]) is int):
		mySum += k[i]
	elif (type(k[i]) is float):
		mySum += k[i]
if (myStr!="" and mySum!=0):
	print "The array you entered is of mixed type"
	print myStr
	print mySum
elif (myStr=="" and mySum!=0):
	print "The array is of integer type"
	print mySum
else:
	print "The array is of string type"
	print myStr