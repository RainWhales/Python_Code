import sys

N_of_Student = int(input())
Student = []

for i in range(N_of_Student):
    name, day, mon, year = sys.stdin.readline().split()
    Student.append((name, int(year), int(mon), int(day)))
    
    
Young = max(Student, key = lambda x : (x[1],x[2],x[3]))
Old = min(Student, key = lambda x : (x[1],x[2],x[3]))

print(Young[0])
print(Old[0])