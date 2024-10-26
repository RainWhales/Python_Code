Num1, Num2 = map(str, input().split())
R_Num1 = int(Num1[::-1])
R_Num2 = int(Num2[::-1])

if R_Num1 > R_Num2:
    print(R_Num1)
else:
    print(R_Num2)
