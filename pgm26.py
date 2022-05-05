# Three digit no is Polyndrome or not 
a=int(input('a=?'))
b=a%10
c=a//10
d=c%10
e=c//10
f=b*100+d*10+e
if f==a:
    print('Polyndrome')
else:
    print('Not Polyndrome')
