T = input()

def test(l1,l2):
    min = 0 
    l2.reverse()
    
    for i in range(len(l1)):
        if l1[i]<=l2[i]:
            min = min + ord(l2[i])-ord(l1[i])
        else: 
            min  = min + ord(l1[i])-ord(l2[i])
    return min

for i in range(T):
    l = raw_input()
    
    if len(l) % 2 == 0:
        l1 = list(l[:len(l)/2])
        l2 = list(l[len(l)/2:])
    else:
        l1 = list(l[:len(l)//2])
        l2 = list(l[len(l)//2+1:])
        
    print test(l1,l2)
