Dial = list(input())
s = 0
for n in Dial:
    if n in 'ABC':
        s += 3
    elif n in 'DEF':
        s += 4
    elif n in 'GHI':
        s += 5
    elif n in 'JKL':
        s += 6
    elif n in 'MNO':
        s += 7
    elif n in 'PQRS':
        s += 8
    elif n in 'TUV':
        s += 9
    elif n in 'WXYZ':
        s += 10
        
print(s)