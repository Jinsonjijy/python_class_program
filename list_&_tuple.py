t=(0,102,3,4,62)
print(t[::-1])
print(t[2:3])


t1=(10,)
print(t1)
print(type(t1))
t2=(12)
print(t2)
print(type(t2))
t=("python")*4
print(t,end=". ")

t=("bmw","benz","ram")
t2=("lamborghini","dodge","chevy")
for x in t:
    print(x)
for x in t:
     print(x,end=".  ")
print(t+t2)



t=("hanoch","aaron",12,13,14)
print (t)
print(type(t))
print(t[1])
for i in t:
    print(i)


n=int(input("enter the number of student:"))
st=[]
for i in range (n):
     
    st.append(input("enter the name of ",
    ))
st.sort() 
print(st)




alist=[1,3,2,5,4,10,9]
alist.sort(reverse=True)
print(alist)
blist=["lamborghini","Ferrari","Koenigsegg","Chevrolet"]
blist.sort(key=len, reverse=True)
print(blist)




n=int(input("enter the number of student:"))
st=[]
for i in range (n):
     
    st.append(input("enter the name of ",
    ))
name=input("enter the name:")  
if name in st:
    print("yes",st.index(name)) 
else:
    print("no")



