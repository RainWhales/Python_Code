import sys

Numbers = []

while True:
    nums = list(map(int, sys.stdin.readline().split()))

    if nums == [0,0]:
        break
    
    Numbers.append(nums)
    
for i in range(len(Numbers)):
    if Numbers[i][0] > Numbers[i][1]:
        print('Yes')
    else:
        print('No')
        