my_list = [1, 2, 3, 4, 5]

# Identity operators
a = my_list
b = [1, 2, 3, 4, 5]

is_same_object = a is my_list
is_not_same_object = b is not my_list

# Membership operators
element_in_list = 3 in my_list
element_not_in_list = 6 not in my_list

print("a is my_list:", is_same_object)
print("b is not my_list:", is_not_same_object)
print("3 in my_list:", element_in_list)
print("6 not in my_list:", element_not_in_list)

# ===== Cursor Additions =====

# Note: Two approaches to operator evaluation - same result, different timing

# Approach 1: Pre-definition (used above)
# - Calculate the operation result first
# - Store in descriptive variable
# - Print the stored boolean
is_same_object = a is my_list    # ← Evaluation happens HERE first
print("result:", is_same_object) # ← Just prints the stored boolean

# Approach 2: Within print (alternative)
# - Calculate and print in one step
print(f"result: {a is my_list}") # ← Evaluation happens HERE during print

# Both output the exact same thing: same result, just different timing

# When to use each:
# Pre-definition: When you need to reuse the boolean result multiple times
# Within print: When you just need it once for display

# Example where pre-definition is better:
user_input = 3
valid_options = [1, 2, 3, 4, 5]
is_valid = user_input in valid_options  # Store result for reuse
if is_valid:
    print("Processing valid input...")
print(f"Input valid: {is_valid}")  # Reusing the same boolean

# Example where within-print is fine:
print(f"Input valid: {user_input in valid_options}")  # One-time check
