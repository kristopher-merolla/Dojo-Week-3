# Assignment: Names

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

# print users["Students"][0]["first_name"]
# print users[users.keys()[0]][0]["first_name"]
# print users[users.keys()[0]][0]["last_name"]
# print len(users.keys())

def userStepper(d):
    for i in range (0,len(users.keys())): # This first loop will go through the outer keys "Students" and "Instructors"
        print users.keys()[i]
        for j in range (0,len(users[users.keys()[i]])): # This second loop goes through each outer key array elements
            whole_name = users[users.keys()[i]][j]["first_name"]+users[users.keys()[i]][j]["last_name"]
            print j+1,"-",whole_name,"-",len(whole_name)

userStepper(users)

# def dictionaryStepper(d):
#     for i in range (len(d)):
#         print d[i]["first_name"],
#         print d[i]["last_name"]

# dictionaryStepper(students)

# ------------------------------------------------------------------------------------------
# Write the following function.

# Part I
# Given the following list:

# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
# Create a program that outputs:

# Michael Jordan
# John Rosales
# Mark Guillen
# KB Tonel

# Part II
# Now, given the following dictionary:

# users = {
#  'Students': [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
#   ],
#  'Instructors': [
#      {'first_name' : 'Michael', 'last_name' : 'Choi'},
#      {'first_name' : 'Martin', 'last_name' : 'Puryear'}
#   ]
#  }

# Create a program that prints the following format (including number of characters in each combined name):

# Students
# 1 - MICHAEL JORDAN - 13
# 2 - JOHN ROSALES - 11
# 3 - MARK GUILLEN - 11
# 4 - KB TONEL - 7
# Instructors
# 1 - MICHAEL CHOI - 11
# 2 - MARTIN PURYEAR - 13

# Note: The majority of data we will manipulate as web developers will be hashed in a dictionary using key-value pairs. 
# Repeat this assignment a few times to really get the hang of unpacking dictionaries, as it's a very common requirement of any web application.