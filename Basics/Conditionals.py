#An if statement eveluates a statement and only executes if it is true

#A variable to evaluate in the if statement
b = True

#When comparing variable like b to another value, you must use == and not =. == checks the variables value where as = assigns a new value to that variable
#You must also indent all the code that goes in the if statment.
if b == True:
	print("b is True")

c = False

#this will not print anything because c is False
if c == True:
	print("c is True")

# you can do this with a number or a string too
i = 10
if i == 10:
	print(i)

s = "t"
if s == "t":
	print("This will print")

#if statements can also be used to evaluate multiple possibilities with the elif statement
s = "e"
if s == "t":
	print("This will not print")
elif s == "e":
	print("This will print")

#finally use else to do something if non of your conditional statements are executed

s = "d"
if s == "t":
	print("This will not print")
elif s == "e":
	print("This will not print")
else:
	print("This will print")

#Try some if statements of your own
