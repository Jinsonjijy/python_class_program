

n=input("enter the word or the sentence:")
count=0
print(len(n))
for i in n:
    # print(i)
    if i in "aeiouAEIOU":
        count=count+1
print(count)


