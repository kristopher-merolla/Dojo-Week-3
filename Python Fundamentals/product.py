# Assignment: Product
# The owner of a store wants a program to track products. Create a product class to fill the following requirements.

# Product class should have these attributes:
# Price
# Item Name
# Weight
# Brand
# Cost
# Status: default "for sale"

# Product class should have these methods:
# Sell: changes status to "sold"
# Add tax: takes tax as a decimal amount as a parameter and returns the price of the item including sales tax
# Return: takes reason for return as a parameter and changes status accordingly. 
	# If the item is being returned because it is defective change status to defective and change price to 0. 
	# If it is being returned in the box, like new mark it as for sale. If the box has been opened set status to used and apply a 20% discount.
# Display Info: show all product details.
# Every method that doesn't have to return something should return self so methods can be chained.

# ---------------------------------------------------------------

class Product(object):
	def __init__(self,name,price,weight,brand,cost):
		self.name = name
		self.price = price
		self.weight = weight
		self.brand = brand
		self.cost = cost
		self.status = "for sale"
		self.profit = self.price - self.cost # Added a variable profit which will be the difference of the price and cost
		print "New Product Created!"
	
	def sell(self):
		self.status = "sold"
		return self

	def add_tax(self,tax): #add_tax takes in the tax (as a decimal) and then adds that to the price
		self.tax = tax
		self.price *= (self.tax+1)
		return self.price

	def return_item(self,reason):
		self.reason = reason
		if (self.reason == "defective"):
			self.status = "defective"
			self.price = 0
		elif (self.reason == "in box"):
			self.status = "for sale"
			print "tax is",self.tax
			self.price /= 1+self.tax # this resets the price to the pre-taxed price
		else:
			self.status = "used"
			self.price /= 1+self.tax # this resets the price to the pre-taxed price
			self.price *= 0.8
		return self

	def display_info(self):
		print self.name
		print "The status is",self.status
		print "The price is $",self.price
		print "The weight is",self.weight
		print "The brand is",self.brand
		print "The cost to me is $",self.cost


product1 = Product("Chips",1.5,"16oz","Pringles",0.5)
product1.display_info()
product1.sell().add_tax(0.10) # add a 10% tax (0.1) to the product1 product instance and sells it
# product1.return_item("defective")
# product1.return_item("in box")
product1.return_item("used")
product1.display_info()
