S = input()
S = S.upper()
S_set = set(S)
S_dict = {}

for i in S_set:
    S_dict[i] = S.count(i)
    
print(S_dict)