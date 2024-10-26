a, b = map(int, input().split())
mult = a*b

while True:
    r = a % b
    if r == 0:
        break
    a = b
    b = r # r이 0 이 될 때, b가 최대공약수.
    
print(b)
print(int(mult/b))