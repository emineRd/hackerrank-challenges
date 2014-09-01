T = input()

def test(l1,l2):
    cpy = list(l2)
    min = 0 
    
    for i in l1: 
        if i not in cpy: 
            min += 1
        else:
            cpy.remove(i)

           
    return min
            
for i in range(T):
    
    word = raw_input()
    
    if len(word) % 2 == 1 : 
        print -1
        
    else:
        l1 = []
        l2 = []
        c = 0 
        for j in word:
            if c < len(word)/2:
                l1.append(j)
            else:
                l2.append(j)
            c +=1
           
        print test(l1,l2)
