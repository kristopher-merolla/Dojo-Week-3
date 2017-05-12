

alpha = ["M","D","C","L","X","V","I"]
rom_num = [1000,500,100,50,10,5,1]
roman_numerals = ""

def romanNumerals(num):
	for i in range (len(rom_num)):
		print "i: ",i," - ",
		print (num-num%rom_num[i])%rom_num[i]
		if ((num-num%rom_num[i])%rom_num[i]==9):
			print yep

romanNumerals(9494)