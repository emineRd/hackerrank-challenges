
N = input()

a = raw_input().split()
L = []

for i in range(N):
    L.append(int(a[i]))
     
L.sort()

D = [] #list of differences

for i in range(N-1):
    D.append(L[i+1]-L[i])
    if D[i] < 0:
        D[i] = -D[i]
        
D.sort()
min = D[0]

for i in range(N-1):
    if L[i+1]-L[i] == min or L[i+1]-L[i] == -min :
        print L[i], L[i+1],
        
