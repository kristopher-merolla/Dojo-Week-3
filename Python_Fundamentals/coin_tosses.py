# Assignment: Coin Tosses
# Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.

# --------------------------------------------------------

def coin_toss(tossNum):
	import random
	heads = 0 # coin_toss_val of 1 = heads
	tails = 0 # coin_toss_val of 0 = tails
	for i in range (tossNum+1):
		coin_toss_val = int(round(random.random()))
		print "Attempt #",i,": Throwing a coin... It's a",
		if (coin_toss_val == 1):
			heads += 1
			print "head! ... Got",heads,"head(s) so far and",tails,"tail(s) so far"
		else:
			tails += 1
			print "tail! ... Got",heads,"head(s) so far and",tails,"tail(s) so far"

coin_toss(5000)
