a=int(input("Enter the number a:"))
b=int(input("Enter the number b:"))
c=int(input("Enter the number c:"))
d=int(input("Enter the number d:"))

if(a>d):
    f1=a
else:
    f1=d
    
if(b>c):
    f2=b
else:
    f2=c
    if(f2>f1):
        print(str(f2)+"is greatest")
    else:    
        print(str(f1)+"is greatest")