def check_age():
    try:
        age = int(input("Enter your age: "))
        if age <= 0:
            print("Error: Age must be a positive number.")
        else:
            if age % 2 == 0:
                print(f"Your age {age} is even.")
            else:
                print(f"Your age {age} is odd.")
    except ValueError:
        print("Error: Invalid input! Please enter a valid number.")

check_age()
