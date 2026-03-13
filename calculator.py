def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b


def calculator():
    while True:
        print("\nSimple Calculator")
        print("1. +")
        print("2. -")
        print("3. *")
        print("4. /")
        print("5. Clear")
        print("6. Exit")

        choice = input("Choose operation: ")

        if choice == "6":
            print("Goodbye!")
            break

        if choice == "5":
            print("\nCalculator cleared\n")
            continue

        if choice not in ["1","2","3","4"]:
            print("Invalid choice")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers")
            continue

        if choice == "1":
            print("Result:", add(num1, num2))
        elif choice == "2":
            print("Result:", subtract(num1, num2))
        elif choice == "3":
            print("Result:", multiply(num1, num2))
        elif choice == "4":
            print("Result:", divide(num1, num2))


if __name__ == "__main__":
    calculator()
