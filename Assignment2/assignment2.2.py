Name=str(input("enter name of student"))
Class1=str(input("enter class of student"))
print("ENTER MARKS OF FIVE SUBJECT")
Total_marks=0
Math=int(input("Enter marks of maths out of 100"))
Total_marks+=Math
C_lang=int (input("Enter marks of c language out of 100"))
Total_marks+=C_lang
DSA=int(input("Enter the marks of DSA out of 100"))
Total_marks+=DSA
JAVA=int (input("Enter marks of java out of 100"))
Total_marks+=JAVA
python=int(input("Enter marks of python out of 100"))
Total_marks+=python
Per=Total_marks/5
print( "Name","Class1","Total_marks","Percentage",sep="  ")
print(Name,Class1,Total_marks,Per,sep="    ")
if (Per>=95) and (Per<=100):
    print("grade A")
elif (Per>=90)and(Per<95):
    print("grade B")
else:
    print("fail")
