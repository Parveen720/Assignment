#practice for Tuple,Dictionary,Set
#Tuples
tuple1=(1,2,3,4,5,6,"parveen")
print(tuple1)
print(tuple1[3])
num1=len(tuple1)
for x in range(0,num1):
    print(tuple1[x])
tuple2=(10,20,30)
print(tuple1+tuple2)
tuple3=(tuple1,tuple2)
print(tuple3)
print(tuple1[0:])
list1=[1,2,3,4,5,6,7]
tuple4=tuple(list1)
print(tuple4)
#set
set1={"apple","banana","mango",True,1}
print(set1)
set1.add("cheery")
set2={"parveen","yadav",}
print(set1.union(set2))
print(set1.intersection(set2))
set3=set1.intersection_update(set2)
print(set3)
set4=set1.difference(set2)
print(set4)
if set1==set2:
    print("true")
else:
    print("false")


