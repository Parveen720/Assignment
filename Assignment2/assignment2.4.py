#4) Create a billing program using list. Program should have options to
# 1. Create Bill
# 2. Add items to the bill
# 3. Display Item Price and total bill amount
# 4. Display Total
# 5. Exit
from random import choice

Bill=[]
while True:
    print('''
1.Enter 1 for create new Bill
2.Enter 2 for Create Bill
3.Enter 3 for Display Item Price and total bill amount
4.Enter 4 for Display Total
5.Enter 5 for Exit
''')
    choice1=int(input("enter your choice"))
    if choice1==1:
        Bill.clear()
        print("NEW BILL")
    elif choice1==2:
        Total_product=int(input("Enter the total product purchased"))
        for i in range(0,Total_product):
            Item=input("Enter name of the item")
            price=int(input("Enter the price of the item"))
            Quantity=int(input("Enter total number of quantity of item purchased"))
            Bill.append([Item,price,Quantity])
    elif choice1==3:
        if not Bill:
            print("There is  no BILL")
        else:
            for Item,price,Quan in Bill:
                print("Item Name:",Item)
                subtotal=price*Quan
                print("price of single item:",price)
                print("total price of item:",subtotal)

    elif choice1==4:
        Total=sum(price*Quantity for Item,price,Quantity in Bill)
        print("Total_Amount =",Total)
    elif choice1==5:
        print("task complete")
        break
    else:
        print("Invalid Choice")

