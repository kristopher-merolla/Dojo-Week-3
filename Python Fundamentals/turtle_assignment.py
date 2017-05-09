# try this either as a .py file or in the python shell
import turtle
# the distance we want the pointer to travel each time
# DIST = 5
# for x in range(0,10):
# 	print "x", x
# 	for y in range(1,5):
# 		print "y", y
#         # turn the pointer 90 degrees to the right
# 		turtle.right(45)
#         # advance according to set distance
# 		turtle.forward(DIST)
# 		turtle.right(45)
#     # add to set distance
# 	DIST += 5
# # # The above for loop prints a pyramid

from turtle import *

def moveUp(a):
	left(90)
	forward(a)
	right(90)

def moveDown(b):
	right(90)
	forward(b)
	left(90)

def moveUpRight(c):
	left(45)
	forward(c)
	right(45)

def moveUpLeft(d):
	right(45)
	forward(d)
	left(45)

def moveDownLeft(e):
	right(135)
	forward(e)
	left(135)

def moveDownRight(f):
	right(45)
	forward(f)
	left(45)

def moveRight(g):
	forward(g)

def moveLeft(h):
	left(180)
	forward(h)
	right(180)

# Draws K
moveUp(50)
moveDown(25)
moveUpRight(35.35)
moveDownLeft(35.35)
moveDownRight(35.35)
# K

# Draws L
moveRight(25)
moveUp(50)
moveDown(50)
moveRight(25)
# L

# Draws M
moveRight(25)
moveUp(50)
moveDownRight(35.35)
moveUpRight(35.35)
moveDown(50)
# M

done() # this will allow the drawing to pause once completed

# # # The below code prints a star
# from turtle import *

# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()