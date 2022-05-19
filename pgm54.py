# Character is Lower or not using ASCII value
a=(input('a='))
d= ord(a)
if d<=97 and d<=122:
    print('Character is Lowercase')
else:
    print('Character is Not Lowercase')