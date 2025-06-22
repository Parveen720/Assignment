#Input 2 strings concatinate them and store in another variable. then perform generally used
# string methods on it like
str1=str(input("Enter the first string"))
str2=str(input("Enter the second string"))
str3=str1+str2
print(str)

print("to print the string in 80 space")
print(str3.center(80))
print("to printt the string in uppercase")
print(str3.upper())
print("to print the string in lowercase")
print(str3.lower())
print("to print the start with a")
print(str3.startswith('t'))
print("count total number of any character in an string")
print(str3.count("a"))
print("string end with any character")
print(str3.endswith("v"))
print("modify string according to any given mapping")
l='pven'
e='1234'
encoding=str3.maketrans(l,e)
print(str3.translate(encoding))
print("split the string")
print(str3.splitlines())