intStdtime = list(map(int, input().split()))
intStdtime[1] -= 45

if intStdtime[1] < 0:
    intStdtime[0] -= 1
    intStdtime[1] += 60
    if intStdtime[0] < 0:
        intStdtime[0] += 24

print(intStdtime[0], intStdtime[1])