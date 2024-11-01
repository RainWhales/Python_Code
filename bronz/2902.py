S = input()
S_list = S.split('-')

Short = [x[0] for x in S_list]
print(''.join(Short))