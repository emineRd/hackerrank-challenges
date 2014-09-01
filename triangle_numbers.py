T = input()

for i in range(T):
    N = input()
    
    if N % 2 == 1:   #every row begins with 1, every other row has an even number in a second position [1,2,3,4,5...]
        print 2
    elif N % 4 == 0: # N % 4 == 0 and N % 4 == 1 --> even numbers
        print 3
    elif N % 4 == 2: 
        print 4
    else: print -1
