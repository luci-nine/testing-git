x = input('Enter the word:  ')
y = x
m = len(x)
j =''
 
for i in range(m-1 , -1 ,-1):
    #print(x[i] ,end='')
    j=j+x[i]
    
if y== j:
    print('It is palindrome.')
    
else:
    print('It is not palindrome word')