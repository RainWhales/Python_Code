import sys

Score = {x : sum(map(int, sys.stdin.readline().split())) for x in range(1, 6)}

Winner = max(Score, key = Score.get)

print(f'{Winner} {Score[Winner]}')