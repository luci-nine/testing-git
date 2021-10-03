x=int(input('Enter the number:  '))

y=x
d=0

while x> 0:
    a = x%10
    d = d+a**3
    x = int(x/10)
    
    
if y==d:
    print('It is an Armstrong number')
else:
    print('It is not an Armlstrong number')