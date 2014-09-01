# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())

def buy(N, C, M):
    cokoladice = N / C
    ostatak = 0
    omoti = cokoladice
    besplatne  = 0
    
    
    
    if cokoladice >= M : 
        while omoti >= M:
            besplatne = omoti // M 
            ostatak = omoti % M
            
            omoti = omoti + besplatne - besplatne*M 
            
            cokoladice += besplatne 

    return cokoladice


for i in range (0,T):
    A,B,C1 = [int(x) for x in raw_input().split(' ')]
 
    print buy(A,B,C1)

