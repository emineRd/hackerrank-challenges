import math

word = raw_input()
x = len(word)
mtrx = []

#calculate constraints
a = int(math.floor(math.sqrt(x)))
b = int(math.ceil(math.sqrt(x)))

if x<= b*b:
	m = b
	n = b 
	
	if x <= a*b:
		m = a
		if x <= a*a:
			n = a

#create matrix
for i in range(m+1):
	mtrx.append([])
	for j in range(n+1):
		mtrx[i].append(' ')


#put word to matrix
for i in range(m):
	for j in range(n+1):
		if i*n+j < x:
			mtrx[i][j] = word[i*n+j]

w = ''

#print out code
for j in range(n):
	for i in range(m):
		if mtrx[i][j] != ' ':
			w +=mtrx[i][j]
		print w, 
		w = ''


