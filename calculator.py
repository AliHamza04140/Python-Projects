x = float(input("Enter first number:"))
y = float(input("Enter second number:"))
operation = input("Enter operation (+, -, *, /):")

if operation == "+":
    result = x + y
    print(f"The Result of {x} + {y} is {result}")
elif operation == "-":
    result = x - y
    print(f"The Result of {x} - {y} is {result}")
elif operation == "*":
    result = x * y
    print(f"The Result of {x} * {y} is {result}")
elif operation == "/":
    if y== 0:
        print("Error: Cannot divide by zero.")
    else:
        result = x / y
        print(f"The Result of {x} / {y} is {result}")
else:
    print("Invalid operation. Please enter a valid operation (+, -, *, /).")               