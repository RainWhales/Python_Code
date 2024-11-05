import sys
S = []

while True:
    S.append(sys.stdin.readline().rstrip())
    if S[-1] == '':
        break
    
print('\n'.join(S))