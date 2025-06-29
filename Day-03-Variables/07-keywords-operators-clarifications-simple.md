# Keywords and Operators Clarifications - Simple

---
## **⚡ WHEN CONFUSED - READ THIS FIRST! ⚡**
**Assignment operators do the action THEN you print the result separately!**
**`not` works on ONE thing, `and`/`or` work on TWO things!**
---

## **1. Assignment Operators - Do THEN Print**

**❌ WRONG - Trying to print the assignment action:**
```python
total = 10
print(total += 5)  # ERROR! Can't print the assignment action
```

**✅ RIGHT - Do the assignment THEN print the result:**
```python
total = 10
total += 5        # Do the assignment first
print(total)      # Then print the result: 15
```

**Why this happens:**
- `+=` is an **action**, not a **value**
- You can't print actions, only values
- Do the action first, then print what it created

## **2. All Assignment Operators Work the Same Way**

```python
# Start with a number
count = 20

# Do each assignment action
count += 10   # Add 10: count becomes 30
print(count)  # Print: 30

count -= 5    # Subtract 5: count becomes 25  
print(count)  # Print: 25

count *= 2    # Multiply by 2: count becomes 50
print(count)  # Print: 50

count /= 4    # Divide by 4: count becomes 12.5
print(count)  # Print: 12.5
```

## **3. Logical Operators - not vs and/or**

**`not` works on ONE thing:**
```python
x = True
y = False

print(not x)      # ✅ CORRECT: not True = False
print(not y)      # ✅ CORRECT: not False = True

# print(x not y)  # ❌ WRONG: Can't use 'not' between two things
```

**`and`/`or` work on TWO things:**
```python
x = True
y = False

print(x and y)    # ✅ CORRECT: True and False = False
print(x or y)     # ✅ CORRECT: True or False = True

# You can combine them:
print(not x and y)     # ✅ CORRECT: (not True) and False = False and False = False
print(x or not y)      # ✅ CORRECT: True or (not False) = True or True = True
```

## **4. Boolean Variables vs Numbers**

**Boolean variables store True/False:**
```python
x = True      # Boolean variable
y = False     # Boolean variable

# Use with logical operators
print(x and y)    # False
print(x or y)     # True
print(not x)      # False
```

**Number variables store numbers:**
```python
a = 1         # Number variable
b = 2         # Number variable

# Use with math operators
print(a + b)      # 3
print(a * b)      # 2
print(a > b)      # False (comparison result is boolean)
```

**Don't mix them up:**
```python
# Boolean operations
x = True
y = False
result = x and y  # Boolean result: False

# Math operations  
a = 1
b = 2
result = a + b    # Number result: 3

# Comparison operations (create booleans from numbers)
result = a > b    # Boolean result: False
result = a < b    # Boolean result: True
```

## **5. Keywords You Can't Use as Variable Names**

**Reserved words (don't use these as variable names):**
```python
# ❌ DON'T DO THIS:
# and = 5        # ERROR! 'and' is a keyword
# or = 10        # ERROR! 'or' is a keyword  
# not = True     # ERROR! 'not' is a keyword
# if = "hello"   # ERROR! 'if' is a keyword

# ✅ DO THIS INSTEAD:
result_and = 5
result_or = 10
is_not_valid = True
condition_if = "hello"
```

**Common keywords to avoid:**
- `and`, `or`, `not`
- `if`, `else`, `elif`
- `for`, `while`, `in`
- `def`, `return`, `class`
- `True`, `False`, `None`
- `import`, `from`, `as`

## **6. Step-by-Step Assignment Pattern**

**Always follow this pattern:**
```python
# Step 1: Start with a variable
score = 100

# Step 2: Do the assignment operation
score += 25

# Step 3: Check the result  
print(f"New score: {score}")  # New score: 125

# Step 4: Do another operation
score -= 15

# Step 5: Check the result again
print(f"Final score: {score}")  # Final score: 110
```

## **7. Testing Logical Operators**

**Test with different combinations:**
```python
# Create boolean variables
is_logged_in = True
has_permission = False

# Test all combinations
print("Logged in AND has permission:", is_logged_in and has_permission)  # False
print("Logged in OR has permission:", is_logged_in or has_permission)    # True
print("NOT logged in:", not is_logged_in)                               # False
print("NOT has permission:", not has_permission)                        # True

# Combined logic
print("Logged in but NO permission:", is_logged_in and not has_permission)  # True
```

## **8. Common Mistakes and Fixes**

**Mistake 1: Assignment in print**
```python
# ❌ WRONG
value = 10
# print(value += 5)  # ERROR!

# ✅ RIGHT  
value = 10
value += 5
print(value)  # 15
```

**Mistake 2: Wrong logical operator usage**
```python
# ❌ WRONG
x = True
y = False
# print(x not y)  # ERROR!

# ✅ RIGHT
x = True  
y = False
print(not x)      # False
print(x and y)    # False
print(x or y)     # True
```

**Mistake 3: Using keywords as variables**
```python
# ❌ WRONG
# if = "hello"    # ERROR!
# and = 5         # ERROR!

# ✅ RIGHT
condition = "hello"
result = 5
```

## **Remember:**
1. **Assignment operators**: Do the action, THEN print
2. **`not`**: Works on one thing at a time
3. **`and`/`or`**: Work on two things at a time  
4. **Keywords**: Can't be used as variable names
5. **Boolean vs numbers**: Different types, different operators 