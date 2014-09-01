T = input()

def test(A,B,K):
    counted = []
    for p in A:
        if p not in counted:
            counted.append(p)
            c = A.count(p)
            #count elements in B that are greater than K-p
            beastmaster = 0
            for beast in B: 
                if beast >= K-p:
                    beastmaster += 1
             
            
            if c <= beastmaster:
                pass
            else: 
                return "NO"
    return "YES"

for i in range(T):
    A = []
    B = []
    l = raw_input().split()
    N = int(l[0])
    K = int(l[1])

    first = raw_input().split()
    second = raw_input().split()
    for j in range(N):
        A.append(int(first[j]))
        B.append(int(second[j]))
    
    A.sort()
    B.sort()
    print test(A,B,K)
