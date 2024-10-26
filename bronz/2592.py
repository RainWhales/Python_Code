# Counter 함수 일부러 이용하지 않음.

import sys

Nums = [int(sys.stdin.readline()) for x in range(10)]
Count_D = {}
for i in Nums:
    try: Count_D[i] += 1
    except: Count_D[i] = 1
    
print(sum(Nums)/len(Nums))
print(max(Count_D, key = Count_D.get))
