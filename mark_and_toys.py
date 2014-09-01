l = raw_input().split()

N = int(l[0])
K = int(l[1])

l = raw_input().split()
toys = []
for i in range(N):
    toys.append(int(l[i]))
    
toys.sort()

def test():
    spent = 0 
    remain = K
    num_toys = 0
    
    for price in toys: 
        if remain >= price: 
            spent += price
            remain -= price
            num_toys += 1
    
    print num_toys
    
test()
            
        
