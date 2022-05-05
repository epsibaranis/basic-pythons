# Character is Upper, Lower, Digit or special character using ASCII value
a=str(input('a='))
d= ord(a)
if d>=65 and d<=90:
    print('Uppercase')
elif d>=97 and d<=122:
    print('Lowercase')
elif d>=48 and d<=57:
    print('Digit')
else:
    print('Special character')
    
