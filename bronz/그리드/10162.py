#처음 푼 풀이

Time = int(input())

A = 300
B = 60
C = 10

A_n = 0
B_n = 0
C_n = 0

if Time >= A:
    while Time >= A:
        Time -= A
        A_n += 1
        if Time == 0:
            print(f'{A_n} {B_n} {C_n}')
            break
    
        
        

if Time >= B and Time != 0:   
    while Time >= B:
        Time -= B
        B_n += 1
        if Time == 0:
            print(f'{A_n} {B_n} {C_n}')
            break
    
       
       
if Time >= C and Time % C == 0 and Time != 0:
    while True:
        Time -= C
        C_n += 1
        if Time == 0:
            print(f'{A_n} {B_n} {C_n}')
            break

elif Time == 0:
    pass
        
else:
    print(-1)
    
""" t = int(input())

time_types = [300, 60, 10]
result = []
for time in time_types :
    n = t // time
    t = t % time
        
    result.append(n)
        
if t > 0 :
    print("-1")
        
else :
    for i in range(3) :
        print(result[i], end=" ")
        
         """ # 한 수 배운 깔끔한 풀이