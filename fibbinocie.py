a=0
b=1
n=input("enter the range:")
i=0
c=0
print(a,b)
while(i<int(n)):
    a=b
    b=c
    c=a+b
    print(str(c))
    i=i+1