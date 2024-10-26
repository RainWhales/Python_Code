N = int(input())
Score = list(map(int, input().split()))

New_Score = [x/max(Score)*100 for x in Score]

print(sum(New_Score)/N)