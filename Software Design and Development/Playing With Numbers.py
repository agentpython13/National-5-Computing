x, y = int(input("Pick two numbers to enter into calculator!")).split()
operation = input("What operation you like to do?")
if operation == "addition":
    print(x + y)
elif operation == "subtraction":
    print(x - y)
elif operation == "multiplication":
    print(x * y)
else:
    print(x / y)
