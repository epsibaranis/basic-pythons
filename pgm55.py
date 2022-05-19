# Character is Digit or not using ASCII value
a=(input('a='))
d= ord(a)
if d<=48 and d<=57:
    print('Character is Digit')
else:
    print('Character is Not Digit')