# Operator is a Arithmatic, Relational, Logical Operator
a=str(input('a=?'))
if a=='+' or a=='-' or a=='*' or a=='/' or a=='%':
    print('Operator is a Arithmatic Operator')
elif a=='>' or a=='<' or a=='=' or a=='<=' or a=='>=' or a=='!=':
    print('Operator is a Relational Operator')
elif a=='and' or a=='or' or a=='not':
    print('Operator is a Logical Operator')
else:
    print('Operator is Not Logical, Arithmatic, Relational operator')