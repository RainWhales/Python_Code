Number = int(input())
Vote = input()

if Vote.count('A') > Vote.count('B'):
    print('A')
elif Vote.count('A') < Vote.count('B'):
    print('B')
else:
    print('Tie')