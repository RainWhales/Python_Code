Start_h, Start_m, Start_s = map(int, input().split(':'))
End_h, End_m, End_s = (map(int, input().split(':')))

if End_s >= Start_s:
    Result_s = End_s  - Start_s
else:
    Result_s = End_s + 60 - Start_s
    End_m -= 1

if End_m >= Start_m:
    Result_m = End_m - Start_m
else:
    Result_m = End_m + 60 - Start_m
    End_h -= 1
    
if End_h >= Start_h:
    Result_h = End_h - Start_h
else:
    Result_h = End_h + 24 - Start_h
    
print(f'{Result_h:02}:{Result_m:02}:{Result_s:02}')
    
    
