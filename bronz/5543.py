import sys

O, M, U, C, S = [int(sys.stdin.readline()) for _ in range(5)]

print(f'{min([O,M,U])+min([C,S])-50}')

con