# def add(scores):
#     sub = str(input("Enter the subject: "))
#     score = int(input("Enter the score: "))
#     scores.append(score)
#     print("Score Added!")

# def calcu(scores):
#     average = sum(scores) / len(scores)
#     print (f"Average Grade: {average}")


# while True:

#     print("\n------------------------")
#     print("Student Grade Calculator")
#     print("------------------------")
#     print("1. Add Score")
#     print("2. Calculate Average")
#     print("3. Exit")
#     choice = int(input("Enter your choice (1-3): "))

#     if choice == 1:
#         add()
#     elif choice == 2:
#         calcu()
#     elif choice == 3:
#         break
#     else:
#         print("Invalid choice! Please select a valid option (1-3).")



def add(scores):
    sub = str(input("Enter the subject: "))
    score = int(input("Enter the score: "))
    scores.append(score)
    print("Score Added!")

def calcu(scores):
    if len(scores) == 0:
        print("No scores available to calculate average.")
    else:
        average = sum(scores) / len(scores)
        print(f"Average Grade: {average:.2f}")

scores = []

while True:
    print("\n------------------------")
    print("Student Grade Calculator")
    print("------------------------")
    print("1. Add Score")
    print("2. Calculate Average")
    print("3. Exit")
    choice = int(input("Enter your choice (1-3): "))

    if choice == 1:
        add(scores)
    elif choice == 2:
        calcu(scores)
    elif choice == 3:
        break
    else:
        print("Invalid choice! Please select a valid option (1-3).")
