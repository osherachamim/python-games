# Prompt for the name until a valid input is provided
while True:
    name = input("What is your name? ")
    if name == "*":
        print("That input is invalid, please enter a valid name.")
    else:
        break

# Prompt for other details
dateOfBirth = input("What is your date of birth? ")
address = input("What is your address? ")
perGoals = input("What is your personal goals? ")

# Print the collected information
print("- Name: " + name)
print("- Date: " + dateOfBirth)
print("- Address: " + address)
print("- Personal Goals: " + perGoals)
