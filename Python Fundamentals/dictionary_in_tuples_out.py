my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

# print len(my_dict) # this returns 3
# print my_dict.keys() # this returns ['Speros','Michael','Jay']
# print my_dict.keys()[1] # this returns Michael
# print my_dict[my_dict.keys()[1]] # this returns (999) 999-9999

# tup1 = (my_dict.keys()[1],my_dict[my_dict.keys()[1]]) # this creates a tuple = ('Michael', '(999) 999-9999')
# print tup1

def dict2tuple(my_dict):
	my_array = []
	for i in range (0,len(my_dict)):
		tup1 = (my_dict.keys()[i],my_dict[my_dict.keys()[i]]) #creates a tuple called "tup1" which is then appended to my_array
		my_array.append(tup1)
	return my_array

print dict2tuple(my_dict)

# ------------------------------------------------------------------------

# Assignment: Dictionary in, tuples out
# Write a function that takes in a dictionary and returns a list of tuples where the first tuple item is the key and the second is the value. Here's an example:

# # function input
# my_dict = {
#   "Speros": "(555) 555-5555",
#   "Michael": "(999) 999-9999",
#   "Jay": "(777) 777-7777"
# }
# #function output
# [("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]