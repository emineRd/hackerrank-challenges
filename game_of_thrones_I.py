string = raw_input()

def test():
	even = 0 
	
	for i in range(25):
		letter = chr(97+i)
		if even > 1 : 
			return False
		if string.count(letter) % 2 == 1:
			even += 1 
	return True

found = False
#Writen the code to find the required palndrome and then assign the
# variable 'found' a value of True or False

found = test()

if not found:
	print("NO")
else:
	print("YES")
