T= input()

def test(k):

    if k % 2 == 0: 
        return (k/2)**2
    else:
        return ((k-1)/2)*((k+1)/2)

for i in range(T):
    k = input()
    
    print test(k)
