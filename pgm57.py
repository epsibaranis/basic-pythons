# Convert uppercase to lowercase using ASCII value
a=str(input('a='))
d= ord(a)
if d>=65 and d<=90:
    e=d+32
    f=chr(e)
    print("Uppercase for the lowercase",f)
          
else:
    print('Not Uppercase')