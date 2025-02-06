def reverse(n):
    return n[::-1]
n=input("enter the word")
temp=n
n=reverse(n)
if temp==n:
    print("the word is palindrome")
else:
    print("the word is not palindrome")