str1=int(input("enter the number"))
num=str(str1)
if num==num[::-1]:
    print("number is palindrome")
else:
    print("not palindrome")