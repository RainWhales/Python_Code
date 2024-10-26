a = list(map(int, input().split()))

a2 = [x**2 for x in a]

print(sum(a2)%10)