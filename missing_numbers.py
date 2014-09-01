n = input()
l1 = raw_input()
m = input()
l2 = raw_input()

A = l1.split()
B = l2.split()

x = int(A[0])

for i in range(x-100,x+100):
    if A.count(str(i)) != B.count(str(i)):
        print i, 
        
