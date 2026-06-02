# ==================================================
# COMPLETE CONDITIONAL STATEMENTS EXAMPLE IN PYTHON
# ==================================================

print("===== Python Conditional Statements Demo =====")

# --------------------------------------------------
# TAKING INPUT
# --------------------------------------------------

age = int(input("Enter your age: "))
salary = int(input("Enter your salary: "))
has_id = input("Do you have ID? (yes/no): ").lower()

# --------------------------------------------------
# BASIC IF
# --------------------------------------------------

print("\n--- Basic IF ---")

if age >= 18:
    print("You are 18 or older")

# --------------------------------------------------
# IF-ELSE
# --------------------------------------------------

print("\n--- IF-ELSE ---")

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# --------------------------------------------------
# IF-ELIF-ELSE
# --------------------------------------------------

print("\n--- IF-ELIF-ELSE ---")

if age < 13:
    print("Category: Child")
elif age < 20:
    print("Category: Teenager")
elif age < 60:
    print("Category: Adult")
else:
    print("Category: Senior Citizen")

# --------------------------------------------------
# NESTED IF
# --------------------------------------------------

print("\n--- Nested IF ---")

if age >= 18:
    if has_id == "yes":
        print("Entry allowed")
    else:
        print("ID card required")
else:
    print("Underage")

# --------------------------------------------------
# USING AND
# --------------------------------------------------

print("\n--- AND Operator ---")

if age >= 21 and salary >= 50000:
    print("Eligible for premium credit card")
else:
    print("Not eligible for premium credit card")

# --------------------------------------------------
# USING OR
# --------------------------------------------------

print("\n--- OR Operator ---")

is_student = True
is_employee = False

if is_student or is_employee:
    print("Discount available")
else:
    print("No discount")

# --------------------------------------------------
# USING NOT
# --------------------------------------------------

print("\n--- NOT Operator ---")

is_banned = False

if not is_banned:
    print("Access granted")
else:
    print("Access denied")

# --------------------------------------------------
# SHORT HAND IF
# --------------------------------------------------

print("\n--- Short Hand IF ---")

if age >= 18: print("Short-hand: Adult")

# --------------------------------------------------
# TERNARY OPERATOR
# --------------------------------------------------

print("\n--- Ternary Operator ---")

status = "Adult" if age >= 18 else "Minor"

print(status)

# --------------------------------------------------
# MULTIPLE CONDITIONS
# --------------------------------------------------

print("\n--- Multiple Conditions ---")

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# --------------------------------------------------
# EVEN OR ODD
# --------------------------------------------------

print("\n--- Even or Odd ---")

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# --------------------------------------------------
# LOGIN SYSTEM EXAMPLE
# --------------------------------------------------

print("\n--- Login System ---")

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")

# --------------------------------------------------
# FINAL MESSAGE
# --------------------------------------------------

print("\n===== Program Finished =====")