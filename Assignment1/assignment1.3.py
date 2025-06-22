operator1=int(input('''
chose 1:For Addition
chose 2:For Substraction
chose 3:for Multiplication
chose 4:For Division
chose 5:For Exponential 
'''))
num1=int(input("Enter first Number"))
num2=int(input("Enter second Number"))
if operator1==1:
    print(f"addition of {num1} + {num2} =",num1+num2)
elif operator1==2:
    print(f"substraction of {num1} - {num2} =",num1-num2)
elif operator1==3:
    print(f"Multiplication of {num1} * {num2} =",num1*num2)
elif operator1==4:
    if num2==0:
        print("division not possible")
    else:
        print(f"division of {num1} / {num2} =",num1/num2)
elif operator1==5:
    print(f"Exponential of {num1} ** {num2} =", num1**num2)
else:
    print("Invalid operator")
    