
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))

# Determine category based on age
if age < 3:
    category = "baby"
elif age < 8:
    category = "child"
elif age < 12:
    category = "preteen"
elif age < 18:
    category = "teenager"
elif age < 30:
    category = "young adult"
elif age < 65:
    category = "adult"
else:
    category = "senior"

print(category)
