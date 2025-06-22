# Input a number from user and find its factorial using for loop
num=int(input("Enter the number for factorial"))
fact=1
for i in range(1,num+1):
    fact*=i
print("factorial","=",fact)