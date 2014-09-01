N = input()

for i in range(N):
    l0 = []
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    l5 = []
    l6 = []
    l = [l0,l1,l2,l3,l4,l5,l6]
    
    keyword = list(raw_input())
    cipher = raw_input()
    answer = ""

    added = []
    k = 0
    t = 0
    while k < len(keyword):
        if keyword[k] not in added:
            l[t].append(keyword[k])
            added.append(keyword[k])
            t += 1
        
        k +=1
        
    #make new alphabet
    k = 0
    original = []
    for c in range(65,91):
        original += chr(c) 
        if chr(c) not in added:
            if k == len(added):
                k = 0
            l[k].append(chr(c))
            k += 1
    
    added.sort()
    
    new_alpha = []
    for a in added: 
        for lst in l: 
            if lst == []:
                break
            if lst[0] == a:
                new_alpha += lst
        
    
    # decode
    for c in cipher: 
        if c == ' ':
            answer += c
        else:
            answer += original[new_alpha.index(c)]
        
    print answer
        
