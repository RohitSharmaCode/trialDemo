# ================================
# STRING SLICING IN PYTHON
# ================================

text = "PythonProgramming"

print("Original String:", text)

# --------------------------------
# BASIC SLICING
# syntax: string[start:end]
# --------------------------------

print("\n--- Basic Slicing ---")

print(text[0:6])      # Python
print(text[6:17])     # Programming
print(text[:6])       # Python (start omitted)
print(text[6:])       # Programming (end omitted)
print(text[:])        # Full string copy

# --------------------------------
# NEGATIVE INDEXING
# --------------------------------

print("\n--- Negative Indexing ---")

print(text[-1])       # g
print(text[-5:])      # mming
print(text[:-5])      # PythonProgra
print(text[-11:-1])   # rogrammin

# --------------------------------
# STEP SLICING
# syntax: string[start:end:step]
# --------------------------------

print("\n--- Step Slicing ---")

print(text[::1])      # Full string
print(text[::2])      # Every 2nd character
print(text[1::2])     # Every 2nd character starting from index 1
print(text[0:10:2])   # Step inside range

# --------------------------------
# REVERSE SLICING
# --------------------------------

print("\n--- Reverse Slicing ---")

print(text[::-1])     # Complete reverse
print(text[::-2])     # Reverse with step 2

# --------------------------------
# REVERSE WITH RANGE
# --------------------------------

print("\n--- Reverse with Range ---")

print(text[10:2:-1])
# Starts from index 10 and moves backward till index 3

print(text[-1:-8:-1])

# --------------------------------
# STRING COPYING
# --------------------------------

print("\n--- String Copy ---")

copy_text = text[:]
print(copy_text)

# --------------------------------
# LAST N CHARACTERS
# --------------------------------

print("\n--- Last N Characters ---")

print(text[-3:])      # Last 3 chars
print(text[-5:])      # Last 5 chars

# --------------------------------
# FIRST N CHARACTERS
# --------------------------------

print("\n--- First N Characters ---")

print(text[:4])       # First 4 chars
print(text[:8])       # First 8 chars

# --------------------------------
# SKIPPING CHARACTERS
# --------------------------------

print("\n--- Skipping Characters ---")

print(text[::3])      # Every 3rd character

# --------------------------------
# PALINDROME CHECK USING SLICING
# --------------------------------

print("\n--- Palindrome Check ---")

word = "madam"

if word == word[::-1]:
    print(word, "is palindrome")
else:
    print(word, "is not palindrome")

# --------------------------------
# REVERSE WORDS USING SLICING
# --------------------------------

print("\n--- Reverse Words ---")

sentence = "Hello World"

print(sentence[::-1])

# --------------------------------
# EDGE CASES
# --------------------------------

print("\n--- Edge Cases ---")

print(text[100:])     # Empty string
print(text[:100])     # Full string safely
print(text[5:2])      # Empty because start > end

# --------------------------------
# IMPORTANT CONCEPT
# end index is EXCLUDED
# --------------------------------

print("\n--- End Index Excluded ---")

print(text[0:6])      # includes 0 to 5 only
