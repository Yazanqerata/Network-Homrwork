import json
name=input('Enter your Name : ')
f=open('C:\\Q3.json ','r')
l=json.load(f)
f.close()
sum=0
z=0
for Question in l[0]:
    print(Question)
    Answr=input('ANSWR : ')
    if Answr==l[1][z]:
        sum=sum+1 
    z=z+1
print(name,':',sum,'/21')
L=dict()
L[name]=sum
f=open('C:\\Q3Result ','w')
json.dump(L,f)
f.close()


    
    