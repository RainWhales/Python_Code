import sys

Nums = []
div_list = []


while True:
    Val = int(input())

    if Val == -1:
        break
    else:
        Nums.append(Val)

for i in Nums:
    div = 1
    while div <= i:
        if i % div == 0 and i != div:
            div_list.append(div)
        div += 1
    if sum(div_list) == i:
            div_str = ' + '.join(map(str, div_list))
            print(f'{i} = {div_str}')
    else:
        print(f'{i} is NOT perfect.')
    
    div_list = []
        
