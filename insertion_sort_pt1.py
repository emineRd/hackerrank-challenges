#!/bin/python
def write_list(l):
    
    for each in l: 
        print each, 
    print

def insertionSort(l):    
    i = N-2
    
    while l[i] > V:
        l[i+1] = l[i]
        i -= 1
        write_list(l)
        if i == -1 : 
            break
        
    l[i+1] = V
    write_list(l)


N = input()
l = [int(i) for i in raw_input().strip().split()]

if N == 1 : 
    print l[0]
elif N == 2 :
    if l[0] < l[1]:
        write_list(l)
    else: 
        print l[1],l[0]
else:
    V = l[N-1]
    insertionSort(l)

