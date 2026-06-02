# ==========================================
# MOST IMPORTANT STRING FUNCTIONS IN PYTHON
# ==========================================

text = "  Python Programming  "

print("Original String:", text)

# ------------------------------------------
# LOWERCASE & UPPERCASE
# ------------------------------------------

print("\n--- lower() and upper() ---")

print(text.lower())
print(text.upper())

# ------------------------------------------
# STRIP FUNCTIONS
# ------------------------------------------

print("\n--- strip(), lstrip(), rstrip() ---")

print(text.strip())     # removes spaces from both sides
print(text.lstrip())    # removes left spaces
print(text.rstrip())    # removes right spaces

# ------------------------------------------
# REPLACE
# ------------------------------------------

print("\n--- replace() ---")

print(text.replace("Python", "Java"))

# ------------------------------------------
# FIND & INDEX
# ------------------------------------------

print("\n--- find() and index() ---")

print(text.find("Programming"))   # returns index
print(text.find("Java"))          # returns -1 if not found

print(text.index("Python"))       # gives index

# index() throws error if not found
# print(text.index("Java"))

# ------------------------------------------
# COUNT
# ------------------------------------------

print("\n--- count() ---")

print(text.count("m"))

# ------------------------------------------
# STARTSWITH & ENDSWITH
# ------------------------------------------

print("\n--- startswith() and endswith() ---")

print(text.strip().startswith("Python"))
print(text.strip().endswith("ing"))

# ------------------------------------------
# SPLIT
# ------------------------------------------

print("\n--- split() ---")

sentence = "apple banana mango"

words = sentence.split()

print(words)

# ------------------------------------------
# JOIN
# ------------------------------------------

print("\n--- join() ---")

words = ["Python", "is", "awesome"]

result = " ".join(words)

print(result)

# ------------------------------------------
# CAPITALIZE & TITLE
# ------------------------------------------

print("\n--- capitalize() and title() ---")

name = "python programming language"

print(name.capitalize())
print(name.title())

# ------------------------------------------
# SWAPCASE
# ------------------------------------------

print("\n--- swapcase() ---")

print("PyThOn".swapcase())

# ------------------------------------------
# IS FUNCTIONS
# ------------------------------------------

print("\n--- isalpha(), isdigit(), isalnum() ---")

print("Python".isalpha())     # only letters
print("12345".isdigit())      # only digits
print("Python123".isalnum())  # letters + digits

# ------------------------------------------
# CENTER
# ------------------------------------------

print("\n--- center() ---")

print("Python".center(20, "-"))

# ------------------------------------------
# ZFILL
# ------------------------------------------

print("\n--- zfill() ---")

print("25".zfill(5))

# ------------------------------------------
# FORMAT
# ------------------------------------------

print("\n--- format() ---")

name = "Rohit"
age = 21

print("My name is {} and I am {} years old".format(name, age))

# ------------------------------------------
# F-STRING (MOST MODERN METHOD)
# ------------------------------------------

print("\n--- f-string ---")

print(f"My name is {name} and I am {age} years old")

# ------------------------------------------
# REMOVEPREFIX & REMOVESUFFIX
# ------------------------------------------

print("\n--- removeprefix() and removesuffix() ---")

url = "https://google.com"

print(url.removeprefix("https://"))

filename = "python.py"

print(filename.removesuffix(".py"))

# ------------------------------------------
# PARTITION
# ------------------------------------------

print("\n--- partition() ---")

email = "user@gmail.com"

print(email.partition("@"))

# ------------------------------------------
# ENCODING
# ------------------------------------------

print("\n--- encode() ---")

print("Python".encode())

# ------------------------------------------
# STRING LENGTH
# ------------------------------------------

print("\n--- len() ---")

print(len("Python"))

# ------------------------------------------
# REVERSING STRING
# ------------------------------------------

print("\n--- Reverse String ---")

word = "Python"

print(word[::-1])

# ------------------------------------------
# CHECK PALINDROME
# ------------------------------------------

print("\n--- Palindrome Check ---")

word = "madam"

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")