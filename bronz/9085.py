T = int(input())

for i in range(T):
    N = int(input())
    N_l = list(map(int, input().split()))
    print(sum(N_l))