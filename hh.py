a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
x = input("Choose operation:")

if x == "a+b":
    print(a+b)
elif x == "a-b":
    print(a-b)
elif x == "b-a":
    print(b-a)
elif x == "a*b":
    print(a*b)
elif x == "a/b":
    print(a/b)
elif x == "b/a":
    print(b/a)
else:
    print("Invalid operator")
