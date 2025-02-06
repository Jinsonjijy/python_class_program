num=int(input("enter the number:"))
temp=num
arm=0
while num>0:
    r=num%10
    arm=arm+(r**3)
    num=num//10
if temp==arm:
    print("armstrong")
else:
    print("not amstrong")


