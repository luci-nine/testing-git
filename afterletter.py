x = input('Enter the word:  ')
y=len(x)
s=''

for i in range(y):
    g=chr(ord(x[i])+1)
    s=s+g
print(s)