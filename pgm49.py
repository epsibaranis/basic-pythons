# smallest of three numbers using Ternary Operation
a=int(input('a=?'))
b=int(input('b=?'))
c=int(input('c=?'))
d=a if a<b else b
e=d if d<c else c
print("smallest of three numbers using Ternary Operation",d)
