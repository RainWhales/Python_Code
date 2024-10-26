import sys

vectors = []
vector_x = []
vector_y = []
Cnt_x = {}
Cnt_y = {}


for i in range(3):
    vectors.append(list(map(int, sys.stdin.readline().split())))
    vector_x.append(vectors[i][0])
    vector_y.append(vectors[i][1])
    
for j in range(len(vector_x)):
    if vector_x[j] in Cnt_x:
        Cnt_x[vector_x[j]] += 1
    else:
        Cnt_x[vector_x[j]] = 1
        
for h in range(len(vector_y)):
    if vector_y[h] in Cnt_y:
        Cnt_y[vector_y[h]] += 1
    else:
        Cnt_y[vector_y[h]] = 1
        
x = min(Cnt_x, key = Cnt_x.get)
y = min(Cnt_y, key = Cnt_y.get)
print(x, y)

        
