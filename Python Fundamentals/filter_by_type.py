# Integer
# If the integer is greater than or equal to 100, print "That's a big number!" If the integer is less than 100, print "That's a small number"
sI = 45
mI = 100
bI = 455
eI = 0
spI = -23

# String
# If the string is greater than or equal to 50 characters print "Long sentence." If the string is shorter than 50 characters print "Short sentence."
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""

# List
# If the length of the list is greater than or equal to 10 print "Big list!" If the list has fewer than 10 values print "Short list."
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

#--------------------------------------
#Integer
arrI = [sI,mI,bI,eI,spI]
print arrI
for i in range (0,len(arrI)):
	if (arrI[i]>=100):
		print "That's a big number!"
	else:
		print "That's a small number"

#String
arrS = [sS,mS,bS,eS]
print arrS
for i in range (0,len(arrS)):
	if (len(arrS[i])>=50):
		print "Long Sentence"
	else:
		print "Short Sentence"

#List
arrL = [aL,mL,lL,eL,spL]
print arrL
for i in range (0,len(arrL)):
	if (len(arrL[i])>=10):
		print "Big list!"
	else:
		print "Short List"