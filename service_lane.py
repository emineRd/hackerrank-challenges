l1 =raw_input().split()
N = int(l1[0])
T = int(l1[1])
width = []
l1 = raw_input().split()
for x in l1: 
    width.append(int(x))    

# test function
def test(i,j):
    answer = 3
    
    k = i 
    while k <= j: 
        if width[k] == 2:
            answer = 2
        if width[k] < 2 :
            answer = 1
            return answer
        k += 1
        
    return answer
        

for i in range(0,T):
    l1 = raw_input().split()
    i = int(l1[0])
    j = int(l1[1])
    
    print test(i,j)
