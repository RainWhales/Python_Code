import sys

Remainder = 0
T = int(input())

for i in range(T):
    Student, Apple = map(int, sys.stdin.readline().split())
    Div = Apple // Student
    Remainder += Apple - (Student*Div)

print(Remainder)