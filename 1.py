def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def get_operation():
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")
    return input("Enter choice (1-5): ")

def get_operands():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b

def calculator():
    while True:
        choice = get_operation()
        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break
        elif choice in ['1', '2', '3', '4']:
            a, b = get_operands()
            try:
                if choice == '1':
                    result = add(a, b)
                elif choice == '2':
                    result = subtract(a, b)
                elif choice == '3':
                    result = multiply(a, b)
                else:  # choice == '4'
                    result = divide(a, b)
                print(f"Result: {result}")
            except ZeroDivisionError as e:
                print(f"Error: {e}")
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    calculator()
