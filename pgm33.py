# Character is Uppercase, Lowercase or Digit
a= str(input('a=?'))
if a>='A' and a<='Z':
    print('Character is Upper case')
elif a>='a' and a<='z':
    print('Character is Lower case')
elif a>='0' and a<='9':
    print('Character is digit')
else:
    print('Character is Special Character')    