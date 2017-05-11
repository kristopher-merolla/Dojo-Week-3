# Assignment: Hospital
# You're going to build a hospital with patients in it! Create a hospital class.

# Before looking at the requirements below, think about what you might want each patient and hospital to be able to do.

# Patient:
# Attributes:

# Id: an id number

# Name

# Allergies

# Bed number: should be none by default

# Hospital
# Attributes:

# Patients: an empty array

# Name: hospital name

# Capacity: an integer indicating the maximum number of patients the hospital can hold.

# Methods:

# Admit: add a patient to the list of patients. Assign the patient a bed number. 
# If the length of the list is >= the capacity do not admit the patient. Return a message either confirming 
# that admission is complete or saying the hospital is full.

# Discharge: look up and remove a patient from the list of patients. Change bed number for that patient back to none.

# This is a challenging assignment. Ask yourself what input each method requires and what output you will need.

# --------------------------------------------------------

class Hospital(object):
	def __init__(self,name,capacity):
		self.patients = [] # creates an empty array (no patients when we first open the hospital!)
		self.beds_taken = 0
		self.name = name
		self.capacity = capacity

	def admit(self): #admit a new patient to the hospital
		if (hospital1.beds_taken >= hospital1.capacity):
			print "Hospital is full, please wait for a discharge"
		else:
			hospital1.beds_taken += 1
			hospital1.patients.append(self.name)
			print "Patient admitted:",self.name
			print "All patient(s) admitted:",hospital1.patients
			# print hospital1.beds_taken

	def discharge(self): #discharge a patient from the hospital
		for i in range (len(hospital1.patients)):
			if (self.name == hospital1.patients[i]):
				print self.name,"removed"
				hospital1.patients.pop(i)
				print "All patient(s) admitted:",hospital1.patients
				hospital1.beds_taken -= 1
				break


class Patient(Hospital):
	def __init__(self,idNum,name,allergies=None,bed=None):
		self.idNum = idNum
		self.name = name
		self.allergies = allergies
		self.bed = bed



hospital1 = Hospital("Stanford Hospital",2)

patient0 = Patient("1","Kris","grass")
patient1 = Patient("2","Jason")
patient2 = Patient("3","Ben","latex")

patient0.admit()
patient1.admit()
patient2.admit() # we try to add "Ben" here, but since capacity for hospital1 = 2, he can't be admitted!

patient0.discharge()
patient2.admit() # now that we've discharged someone, we can add in Ben
patient2.discharge()
patient1.discharge()
