y=input('Enter a binary number : ')
sum=0
z=-1
e=' '
for x in range(len(y)):
    if y[z]=='0':
        
        z=z-1
        pass
    
    elif y[z]=='1':
        
        z=z-1
        sum=sum+2**x
        
    else:
        
        e='error'
        print(e)
        break
if e!='error':
    print('The decimal number is  :',sum)
    