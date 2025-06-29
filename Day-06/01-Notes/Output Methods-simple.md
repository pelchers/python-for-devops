# Output Methods - Simple

## Introduction

Different ways to display results in Python terminal.

## Two Main Methods

### Method 1: Direct Print
```python
def add(a, b):
    return a + b

print(add(5, 3))  # Output: 8
```

### Method 2: Store Then Print
```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8
```

## Key Differences

**Direct Print:**
- One line
- Good for quick testing
- Can't reuse the result

**Store Then Print:**
- Two lines
- Can reuse the result multiple times
- Better for real work

## When to Use Each

**Use Direct Print for:**
- Testing functions
- Simple outputs

**Use Store Then Print for:**
- Results needed multiple times
- Assignment work
- Real programs

## Method 2 Complex: Changing Variables

**Important:** Stored results capture values at the moment the function runs.

```python
def add(a, b):
    return a + b

# Variables that change
a = 5
b = 3

# Store result with current values
result = add(a, b)  # result = 8 (5 + 3)
print(result)       # Output: 8

# Change the variables
a = 10
b = 20

# Stored result does NOT change
print(result)       # Still output: 8 (not 30!)

# To get new result, call function again
new_result = add(a, b)  # new_result = 30 (10 + 20)
print(new_result)       # Output: 30
```

**Key Point:** `result` keeps the old value (8) even when `a` and `b` change!

## Example

```python
# Direct print - testing
print(add(10, 5))

# Store then print - real use
result = add(10, 5)
print(f"Sum: {result}")
print(f"Double: {result * 2}")
print(f"Plus 10: {result + 10}")
``` 