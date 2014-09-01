#!/usr/bin/py
def lonelyinteger(a):
    answer = 0
    lst = list(b)
    
    for x in lst: 
        if lst.count(x) == 1:
            return x
    return answer


if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    
   
    print lonelyinteger(b)
    
    

