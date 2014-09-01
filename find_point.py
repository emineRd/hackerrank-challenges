N = input()

def sym(P,Q):
    
    diff = [Q[0]-P[0],Q[1]-P[1]]
    print Q[0]+diff[0], Q[1]+diff[1]


for l in range(0,N):
    line = raw_input().split()
    P = [int(line[0]),int(line[1])]
    Q = [int(line[2]),int(line[3])]
    
    sym(P,Q)
  
