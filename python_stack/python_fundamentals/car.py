# Assignment: Car

# Create a class called  Car. In the__init__(), allow the user to specify the following attributes: price, speed, fuel, mileage. 
#If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%. 

# Create six different instances of the class Car. In the class have a method called display_all() that returns all the information about the car as a string. 
# In your __init__(), call this display_all() method to display information about the car once the attributes have been defined.

# ----------------------------------------------------------------------

class Car(object):
	def __init__(self,price,speed,fuel,mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if (price > 10000):
			self.tax = 0.15
		else:
			self.tax = 0.12
		self.display_all()

	def display_all(self):
		print "Price:",self.price
		print "Speed:",self.speed
		print "Fuel:",self.fuel
		print "Mileage:",self.mileage
		print "Tax:",self.tax


car1 = Car(2000,"35mph","Full","20mpg")
car2 = Car(15000,"70mph","Full","30mpg")
car3 = Car(7999,"60mph","Full","22mpg")
car4 = Car(107800,"120mph","Half","10mpg")
car5 = Car(1000,"25mph","Empty","18mpg")
car6 = Car(28750,"65mph","Full","25mpg")