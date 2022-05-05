# Character is Uppercase, Lowercase or Digit
a= str(input('a=?'))
if a>='A' and a<='Z':
    print('Upper case')
elif a>='a' and a<='z':
    print('Lower case')
elif a>='0' and a<='9':
    print('digit')
else:
    print('Special Character')
    
    