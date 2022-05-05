# Operator is a Arithmatic, Relational, Logical Operator
a=str(input('a=?'))
if a=='+' or a=='-' or a=='*' or a=='/' or a=='%':
    print('Arithmatic Operator')
elif a=='>' or a=='<' or a=='=' or a=='<=' or a=='>=' or a=='!=':
    print('Relational Operator')
elif a=='and' or a=='or' or a=='not':
    print('Logical Operator')
else:
    print('Not Logical, Arithmatic, Relational operator')

