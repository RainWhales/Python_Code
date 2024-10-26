voca = input()
A = []
B = []

if len(voca) % 2 == 0:
    for i in range(len(voca)):
        if i < len(voca) // 2:
            A.append(voca[i])
        else:
            B.append(voca[i])

else:
    mid = len(voca) // 2
    for i in range(len(voca)):
        if i < mid:
            A.append(voca[i])
        
        elif i ==  mid:
            continue
        
        else:
            B.append(voca[i])
            
B.reverse()
     
if A == B:
    print(1)
else:
    print(0)