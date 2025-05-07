def game():
    max = 1000000000
    attempts = 0

    while attempts < max:    
        guess = 37

        attempts += 1

        num = int(input("Guess the number (1-100): "))
        if num > guess:
            print("Too high!")
        elif num < guess:
            print("Too Low!")
        elif num == guess:
            print(f"Congratulations! You guessed the number in {attempts} attempts")
            break

while True:

    print("\n---------------------")
    print("Number Guessing Game!")
    print("---------------------")
    print("1. Play Number Guessing Game")
    print("2. Exit")
    choice = int(input("Enter your choice (1-2): "))

    if choice == 1:
        game()
    elif choice == 2:
        break
    else:
        print("Invalid choice! Please select a valid option (1-2).")