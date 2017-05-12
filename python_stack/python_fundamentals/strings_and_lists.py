str = "It's thanksgiving day. It's my birthday,too!"
new_str = str.replace("day","month")
# print new_str
x = [2,54,-2,7,12,98]
# print x
# print "The max value in array x is:", max(x)
# print "The min value in array x is:", min(x)
y = ["hello",2,54,-2,7,12,98,"world"]
# print y
# print y[0],y[len(y)-1]
z = [19,2,54,-2,7,12,98,32,10,-3,6]
z.sort()
arr = []
arr.append(z[:(len(z)/2)])
for i in range (len(z)/2,len(z)):
	arr.append(z[i])
print arr