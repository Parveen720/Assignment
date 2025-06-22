lst = [1,2,6,4,8,0,7]
smallest=float("inf")
for i in lst:
    if smallest>i:
        smallest=i
print("smallest","=",smallest)

small=float("inf")
second_smallest=float("inf")
for i in lst:
    if small>i:
        second_smallest=small
        small=i
    elif (second_smallest>i) and (small<=i):
        second_smallest=i
print("smallest","=",small)
print("secondsmallest = ",second_smallest)

largest1=float("-inf")
second_largest=float("-inf")
for i in lst:
    if i>largest1:
        second_largest=largest1
        largest1=i
    elif (i>second_largest) and (i<=largest1):
        second_largest=i
print("secondlargest",second_largest)
