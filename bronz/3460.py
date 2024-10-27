import sys
T = int(input())
S = 1
S_L = [1]
S_R = []
S_RL = []
Two = [int(sys.stdin.readline()) for _ in range(T)]

for i in Two:
    while S <= i:
        S *= 2
        if S > i:
            S /= 2
            break
        S_L.append(S)
        
    S_L.sort(reverse=True)
    for j in S_L:
        if i % j != 0 and i >= j:
            S_RL.append(1)
            i = i % j
        elif i < j:
            S_RL.append(0)
        elif i % j == 0:
            S_RL.append(1)
            i = i % j
    
    C = 0
    C_L = []
    S_RL.reverse()        
    for x in S_RL:
        if x == 1:
            C_L.append(str(C))

        C += 1
    print(' '.join(C_L))
    C = 0
    C_L = []
    S_L = [1]
    S_R = []
    S_RL = []
    S = 1
        
    

    


