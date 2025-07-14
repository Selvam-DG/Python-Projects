def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")

    while True:
        try:
            num1 = float(input("Enter first number (or q to quit): "))
        except ValueError:
            print("Exiting calculator. Till Next time")
            break

        operator = input("Enter operator (+, -, *, /): ")
        if operator not in [ '+', '-', '*', '/']:
            print("Invalid operator! please choose from +, -, *, /")
            continue
        
        try:
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid Number; please try again..")
            continue
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        else:
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            result = num1 / num2
        
        print(f"Result: {num1} {operator} {num2} = {result} \n")

if __name__ == "__main__":
    calculator()
