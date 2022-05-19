# Convert Lowercase to Uppercase using ASCII value
a=str(input('a='))
d= ord(a)
if d>=97 and d<=122:
    e=d-32
    f=chr(e)
    print("Lowercase for the Uppercase:",f)
          
else:
    print('Not lowercase')
