def Rev(x):
    reverse = ''
    for i in str(x):
        reverse = i + reverse
    if reverse[0] == 0:
        del reverse[0]
    R = int(reverse)
    
    return R
    
    
X, Y = map(int, input().split())
print(Rev(Rev(X)+Rev(Y)))