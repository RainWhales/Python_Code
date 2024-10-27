import sys

Score = {x : int(sys.stdin.readline()) for x in range(1, 9)}
Sc = 0
n = []
for i in range(5):
    n.append((max(Score, key = Score.get)))
    Sc += int(Score[n[i]])
    del Score[n[i]]
  

n = map(str, n)
print(Sc)
print(' '.join(sorted(n)))

    