num1=int(input("Enter the first number"))
num2=int(input("enter the second number"))
operator=input('''
Enter the operator
+ for addition
- for subtraction
* for multiplication
/ for divide
other are invalid

''')
def my_fun(num1,num2):
    if operator=='+':
        print("sum of two number is =",num1+num2)
    elif operator=='-':
        print("subtration of two number is=",num1-num2)
    elif operator=='*':
        print("multiplication of two number is=",num1*num2)
    elif operator=='/':
        if num2==0:
            print("division not possible")
        else:
            print("division is =",num1/num2)
    else:
        print("invalid operator")
my_fun(num1,num2)