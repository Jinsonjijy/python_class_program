n=input("enter the word")
temp=n
print(temp)
def reverse(temp):
    return temp[::-1]
temp=reverse(temp)
print(temp)
if temp==n:
    print("the word is a palindrome")
else:
    print("the word is not palindrome")
