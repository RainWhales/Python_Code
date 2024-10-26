bowl = input()
height = 0

for i in range(len(bowl)):
    if i == 0:
        height += 10
    
    else:
        if bowl[i-1] == ')' and bowl[i] == ')':
            height += 5
        elif bowl[i-1] == ')' and bowl[i] == '(':
            height += 10
        elif bowl[i-1] == '(' and bowl[i] == '(':
            height += 5
        else:
            height += 10

print(height)