T = input()

def find_index(cpy, v):
    
    for j in range(len(cpy)): 
        if cpy[j] == v:
            return j+1
        
def test(l,M,N):
    a = 1 
    b = 1
    
    cpy = list(l)
    
    for i in l: 
        cpy.remove(i)
        
        if M-i in cpy: 
            #print 'M-i', M-i
            b = a + find_index(cpy,M-i)
            print a,b
            return
        
        a+=1

        
for i in range(T):
   
    M = input()
    N = input()
    lfake = raw_input().split()
    l = []
    
    for j in lfake:
        l.append(int(j))
        
    test(l,M,N)
