# Assignment: Call Center
# You're creating a program for a call center. Every time a call comes in you need a way to track that call. 
# One of your program's requirements is to store calls in a queue while callers wait to speak with a call center employee.

# You will create two classes. One class should be Call, the other CallCenter.

# Call():
# Create your call class with an init method. Each instance of Call() should have a few attributes:

# - unique id

# - caller name

# - caller phone number

# - time of call

# - reason for call

# The call class should have a display method that prints all call attributes.

# CallCenter():
# Create your call center class with an init method. Each instance of CallCenter() should have the following attributes:

# - calls: should be a list of call objects

# - queue size: should be the length of the call list

# The call center class should have an add method that adds a new call to the end of the call list

# The call center class should have a remove method that removes the call from the beginning of the list (index 0).

# The call center class should have a method called info that shows the name and phone number for each call in the queue 
# as well as the length of the queue.

# ------------------------------------------------------------------------------------------------

class CallCenter(object):
	def __init__(self):
		self.calls = [] # a list of call objects, at first empty
		self.queue_size = 0 # no calls when call center is first opened (initialized)
	def add_new(self):
		call_tupl = (self.idNum,self.name,self.number,self.time,self.reason)
		center.calls.append(call_tupl) # here, center is the name of the CallCenter we initialized from "center = CallCenter()"
		center.queue_size += 1
		# print "Call added to call center queue, currently",center.queue_size,"call(s) in queue"
		# print center.calls
	def remove(self):
		center.queue_size -= 1
		center.calls.pop(0)
		# print "Call removed from queue, currently",center.queue_size,"call(s) in queue"
		# print center.calls
	def info(self):
		print "The call que length is",len(center.calls)
		for i in range (len(center.calls)):
			print center.calls[i][1], center.calls[i][2]


class Call(CallCenter):
	def __init__(self,idNum,name,number,time,reason):
		self.idNum = idNum
		self.name = name
		self.number = number
		self.time = time
		self.reason = reason
	def displayCall(self):
		print self.idNum
		print self.name
		print self.number
		print self.time
		print self.reason


center = CallCenter() #create our call center

call1 = Call("1","Kris","555-123-4567","11:30","Refrigerator is running").add_new()
call2 = Call("2","Sam","555-777-1111","11:45","Where's the beef?").add_new()
call3 = Call("3","Jason","333-400-2888","13:40","Something about a wrench").add_new()

# call1.add_new()
# call2.add_new()

center.info()

# call1.remove()
# call1.remove()


# print center.calls[0][1] # prints out the index 0 caller (first caller) and then the second element (name)





