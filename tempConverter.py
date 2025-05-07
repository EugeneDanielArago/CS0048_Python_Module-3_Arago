def cf():
    c = int(input("Enter temperature in Celsius: "))
    result = (c * 1.8) + 32
    print (f"Temperature in Fahrenheit: {result}")

def fc():
    f = int(input("Enter temperature in Fahrenheit: "))
    result = (f - 32) / 1.8
    print (f"Temperature in Celsius: {result}")


while True:

    print("\n---------------------")
    print("Temperature Converter")
    print("---------------------")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    print("3. Exit")
    choice = int(input("Enter your choice (1-3): "))

    if choice == 1:
        cf()
    elif choice == 2:
        fc()
    elif choice == 3:
        print("Thank You")
        break
    else:
        print("Invalid choice! Please select a valid option (1-3).")