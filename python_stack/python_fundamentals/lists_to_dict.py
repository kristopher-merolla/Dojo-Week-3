

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def list2dict(keyList,valueList):
	new_dict = {} 
	if (len(keyList) != len(valueList)):
		if (len(keyList) > len(valueList)):
			for i in range (0,len(keyList)):
				new_dict[keyList[i]] = valueList[i]
		else:
			for i in range (0,len(keyList)):
				new_dict[valueList[i]] = keyList[i]
	else:
		for i in range (0,len(keyList)):
			new_dict[keyList[i]] = valueList[i]
	return new_dict

print list2dict(name,favorite_animal)

# ----------------------------------------------------------------------------------------

# Create a function that takes in two lists and creates a single dictionary where the first list contains keys and the second values. Assume the lists will be of equal length.

# Your first function will take in two lists containing some strings. Here are two example lists:

# name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
# favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

# Here's some help starting your function.

# def make_dict(arr1, arr2):
#   new_dict = {}
#   # your code here
#   return new_dict

# Hacker Challenge:
# If the lists are of unequal length, the longer list should be used for the keys, the shorter for the values.