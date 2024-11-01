S = input()
S_trans = ''
for i in S:
    if i.isupper():
        S_trans += i.lower()
    else:
        S_trans += i.upper()
        
print(S_trans)