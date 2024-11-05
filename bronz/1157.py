S = input()
S = S.upper()
S_set = set(S)
S_dict = {}

for i in S_set:
    S_dict[i] = S.count(i)

M = [k for k,v in S_dict.items() if v == max(S_dict.values())]

if len(M) >= 2:
    print('?')
else:
    print(''.join(M))