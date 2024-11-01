S = str(input())

Alpa = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Result = []
for a in Alpa:
    Result.append(str(S.find(a)))

print(' '.join(Result))