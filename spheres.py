import math

T = input()
# handle input lines
def create_list():
    l = []
    line = raw_input().split()
    
    for k in line:
        l.append(int(k))
    
    return l

# calculate sphere distance
def distance(x,y):    
    d = math.sqrt((y[0]-x[0])**2+(y[1]-x[1])**2+(y[2]-x[2])**2)

    return d

# calculate new position 
def position(s,a,t):
    
    for i in range(3):
        s[i] = s[i] + t*a[i]
        
    return s
# test collision
def test(s1,a1,r1,s2,a2,r2):
    
    t = 0    
    d0 = distance(s1,s2)
    
    if d0 <= r1+r2 :            #they touch 
        return 'YES'
    
  
    
    t = 0.01
    s1 = position(s1,a1,t)
    s2 = position(s2,a2,t)
    d1 = distance(s1,s2)
    
     
    if d0 == d1: 
        return 'NO'
    
    if d1 <= r1+r2: 
            return 'YES'
    
    while d0 > d1 :
       
        t += 0.005
        d0 = d1
        
        s1 = position(s1,a1,t)
        s2 = position(s2,a2,t)
        d1 = distance(s1,s2)
        
        if d0 == d1: 
            return 'NO'
        
        if d1 <= r1+r2: 
            return 'YES'
        
    return 'NO'

# handle test by test 
for i in range(T):
    s1 = []
    a1 = []
    s2 = []
    a2 = []
    
    l = raw_input().split()
    r1 = int(l[0])
    r2 = int(l[1])
    
    s1 = list(create_list())
    a1 = list(create_list())
    s2 = list(create_list())
    a2 = list(create_list())
    
    
    print test(s1,a1,r1,s2,a2,r2)
    
    
