def add():
    a = int(input("Enter first Number: "))
    b = int(input("Enter second Number: "))
    result = a + b
    print (f"Result is: {result}")

def sub():
    a = int(input("Enter first Number: "))
    b = int(input("Enter second Number: "))
    result = a - b
    print (f"Result is: {result}")

def mul():
    a = int(input("Enter first Number: "))
    b = int(input("Enter second Number: "))
    result = a * b
    print (f"Result is: {result}")

def div():
    a = int(input("Enter first Number: "))
    b = int(input("Enter second Number: "))
    result = a / b
    print (f"Result is: {result}")

while True:

    print("\n-----------------")
    print("Simple Calculator")
    print("-----------------")
    print("1. Addition")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        add()
    elif choice == 2:
        sub()
    elif choice == 3:
        mul()
    elif choice == 4:
        div()
    elif choice == 5:
        break
    else:
        print("Invalid choice! Please select a valid option (1-5).")
    
