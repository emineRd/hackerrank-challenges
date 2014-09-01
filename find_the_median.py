N = input()

l = raw_input().split()
a = []
for i in range(N):
    a.append(int(l[i]))
    
a.sort()

print a[N//2]
