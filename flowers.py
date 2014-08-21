N, K = raw_input().split()
N = int(N)
K = int(K)
C = []

numbers = raw_input()

i = 0 
for number in numbers.split():
	C.append( int(number) )
	i = i+1

C.sort()
C.reverse()


def calc():
	p = 0
	cycle = 1
	result = 0
	while True: 
		for x in range(K):

			if p < len(C):
				result += cycle* C[p]
				p += 1
			else:
				return result
		cycle += 1

print calc() 
