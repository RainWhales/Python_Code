S = input()
R = 0
for i in range((len(S)//10)+1):
    print(S[R:(R+10)])
    R += 10
