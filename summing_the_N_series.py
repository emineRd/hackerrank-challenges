T = input()

def test(n):

    return (n*n) % (10**9 + 7)

for i in range(T):
    n = input()
    
    print test(n)
