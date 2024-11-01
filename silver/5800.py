T = int(input())

for i in range(1, T+1):
    N = list(map(int, input().split()))
    del N[0]
    N.sort(reverse=True)
    Lagest = [N[k-1]-N[k] for k in range(1, len(N))]
    print(f'Class {i}')
    print(f'Max {max(N)},',f'Min {min(N)},',f'Largest gap {max(Lagest)}')
    