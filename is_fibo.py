T = input()

def test(N):
    
    f0 = 0
    f1 = 1
    f = 1
    while f <= N:
        if f == N : 
            return 'IsFibo'
        
        f0 = f
        f = f+ f1
        f1 = f0 
        
    return 'IsNotFibo'
        


for x in range(T):
    N = input()
    
    print test(N)
