# Assignment: Making and Reading from Dictionaries
# Create a dictionary containing some information about yourself. The keys should include name, age, country of birth, favorite language.

# Write a function that will print something like the following as it executes:

# My name is Anna
# My age is 101
# My country of birth is The United States
# My favorite language is Python

# There are two steps to this process, building a dictionary and then gathering all the data from it. 
# Write a function that can take in and print out any dictionary keys and values.

# Note: The majority of data we will manipulate as web developers will be hashed in a dictionary using key-value pairs. 
# Repeat this assignment a few times to really get the hang of unpacking dictionaries, as it's a very common requirement of any web application.

# -------------------------------------------------------


myArrayDictionary = [{"name" : "Anna","age" : 101,"country of birth" : "Canada","favorite language" : "JavaScript"},
{"name" : "Kris","age" : 30,"country of birth" : "The United States","favorite language" : "Python"}]

def readDictionary(d,index,key):
	print "My",key,"is",d[index][key]

x = 0 #here we can set X as the index inside our array of dictionaries

readDictionary(myArrayDictionary,x,"name")
readDictionary(myArrayDictionary,x,"age")
readDictionary(myArrayDictionary,x,"country of birth")
readDictionary(myArrayDictionary,x,"favorite language")