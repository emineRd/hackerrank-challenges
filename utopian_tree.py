T = input()

def test(N):
    h = 1
    
    i = 1
    while i <= N:
        if i % 2 == 1 :
            h = 2*h
        else : 
            h = h+1 
        i += 1     
        
    return h

for i in range(T):
    N = input()
    
    print test(N)
