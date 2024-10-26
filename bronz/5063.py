import sys

Test_Num = int(input())
AD_result = []

for i in range(Test_Num):
    AD = list(map(int, sys.stdin.readline().split()))
    if AD[1]-AD[2] > AD[0]:
        AD_result.append('advertise')
    elif AD[1]-AD[2] == AD[0]:
        AD_result.append('does not matter')
    else:
        AD_result.append('do not advertise')
        
print('\n'.join(AD_result))