# # def sum_numbers(*args):
# #     total = sum(args)
# #     print(f"The sum of the numbers is: {total}")

# # # Call the function with multiple arguments
# # sum_numbers(1, 2, 3, 4, 5)

# # Define a function with a default parameter value
# def greet(name="Guest"):
#     print(f"Hello, {name}!")

# # Call the function without arguments (uses the default value)
# greet()

# # Call the function with an argument (overrides the default value)
# greet("Bob")


# Define an empty dictionary to store student grades
# student_grades = {}

# # Function to add a student and their grade
# def add_student(name, grade):
#     if name in student_grades:
#         print(f"Student {name} already exists. Use update to change the grade.")
#     else:
#         student_grades[name] = grade
#         print(f"Student {name} added with grade {grade}.")

# # Function to update a student's grade
# def update_grade(name, new_grade):
#     if name in student_grades:
#         student_grades[name] = new_grade
#         print(f"Grade for {name} updated to {new_grade}.")
#     else:
#         print(f"Student {name} not found. Use add to add the student.")

# # Function to delete a student's record
# def delete_student(name):
#     if name in student_grades:
#         del student_grades[name]
#         print(f"Student {name} deleted.")
#     else:
#         print(f"Student {name} not found.")

# # Function to display all students and their grades
# def display_grades():
#     if student_grades:
#         print("Student Grades:")
#         for name, grade in student_grades.items():
#             print(f"{name}: {grade}")
#     else:
#         print("No students in the record.")

# # Sample operations to demonstrate the functionality
# add_student("Alice", 90)    # Add Alice with grade 90
# add_student("Bob", 85)      # Add Bob with grade 85
# update_grade("Alice", 95)   # Update Alice's grade to 95
# add_student("Charlie", 88)  # Add Charlie with grade 88
# delete_student("Bob")       # Delete Bob's record
# display_grades()             # Display all students and their grades


# Inventory dictionary: item_name -> quantity
# inventory = {}

# # Function to add stock to an item
# def add_stock(item_name, quantity):
#     if item_name in inventory:
#         inventory[item_name] += quantity
#     else:
#         inventory[item_name] = quantity
#     print(f"Added {quantity} of {item_name}. New stock: {inventory[item_name]}.")

# # Function to remove stock from an item
# def remove_stock(item_name, quantity):
#     if item_name in inventory:
#         if inventory[item_name] >= quantity:
#             inventory[item_name] -= quantity
#             print(f"Removed {quantity} of {item_name}. New stock: {inventory[item_name]}.")
#         else:
#             print(f"Not enough stock of {item_name} to remove {quantity}.")
#     else:
#         print(f"{item_name} not found in inventory.")

# # Function to display the inventory
# def display_inventory():
#     if inventory:
#         print("\nInventory List:")
#         for item_name, quantity in inventory.items():
#             print(f"{item_name}: {quantity}")
#     else:
#         print("Inventory is empty.")

# # Sample operations to demonstrate the functionality
# add_stock("Apples", 50)       # Add 50 Apples
# add_stock("Bananas", 30)      # Add 30 Bananas
# add_stock("Oranges", 40)      # Add 40 Oranges
# remove_stock("Apples", 10)    # Remove 10 Apples
# remove_stock("Bananas", 35)   # Try to remove 35 Bananas (should fail)
# remove_stock("Pears", 5)      # Try to remove Pears (item doesn't exist)
# display_inventory()           # Display the inventory


# Example 3: Creating a tuple using the tuple() constructor
# my_tuple = tuple([1, 2, 3, 4])
# print("Tuple created using tuple() constructor:", my_tuple)


# set2 = set([1, 2, 3, 4])

# Program to check if a character is a vowel or consonant

# Take character input from the user
# char = input("Enter a character: ").lower()  # Convert to lowercase for uniformity

# # Check if the input is a vowel or consonant
# if char in 'aeiou':
#     print(f"{char} is a vowel.")
# else:
#     print(f"{char} is a consonant.")

# Program to check if a given number is prime or not

# Take input from the user
# num = int(input("Enter a number: "))

# # Check if the number is less than or equal to 1
# if num <= 1:
#     print(f"{num} is not a prime number.")
# else:
#     # Assume the number is prime
#     is_prime = True
    
#     # Check for factors from 2 to the square root of the number
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break

#     # Output the result
#     if is_prime:
#         print(f"{num} is a prime number.")
#     else:
#         print(f"{num} is not a prime number.")


# Program to print a right-angled triangle pattern

# # Take input from the user for number of rows
# n = int(input("Enter the number of rows: "))

# # Loop to print each row
# for i in range(1, n + 1):
#     print('*' * i)




# Program to print the first n numbers in the Fibonacci sequence

# Take input from the user for the number of terms
n = int(input("Enter the number of terms: "))

# Initialize the first two Fibonacci numbers
a, b = 0, 1

# Loop to print the Fibonacci sequence
print("Fibonacci sequence:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b  # Update values for the next term
