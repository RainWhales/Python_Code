def RoT13(S):
    code = ''
    for a in S:
        if ord('A') <= ord(a) <= ord('Z'):
            if ord(a)+13 <=ord('Z'):
                code += chr(ord(a)+13)
            else:
                code += chr(ord(chr(ord(a)+13)) - ord('Z') + ord('A'))
            
        elif ord('a') <= ord(a) <= ord('z'):
            
            if ord(a)+13 <=ord('z'):
                code += chr(ord(a)+13)
            else:
                code += chr(ord(chr(ord(a)+13)) - ord('z') + ord('a'))
            
        else:
            code += a
            
    return code

CS = input()

print(RoT13(CS))
