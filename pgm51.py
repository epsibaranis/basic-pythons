#Smallest of three numbers using Nested Ternary Operation
a=int(input('a=?'))
b=int(input('b=?'))
c=int(input('c=?'))
d=(a if a<c else c) if a<b else (b if b<c else c)
print("Smallest of three numbers using Nested Ternary Operation",d)