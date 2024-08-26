# Ask the user to enter their age
while True:
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            print("Age cannot be negative. Please try again.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a whole number.")

# Enter age categories
if age < 0:
    age_group = "Invalid age range"
elif age <= 12:
    age_group = "Child"
elif age <= 19:
    age_group = "Teenager"
elif age <= 64:
    age_group = "Adult"
else:
    age_group = "Senior"

print(f"You are classified as: {age_group}")