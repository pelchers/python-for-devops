# List Examples - Simple

**Examples for each list operation from 01-list.md**

## **1. Creating Lists**
```python
# Different types of lists
numbers = [1, 2, 3, 4, 5]
names = ['alice', 'bob', 'carol']
mixed = [1, 'hello', 3.14, True]
empty = []
```

## **2. List Indexing**
```python
fruits = ['apple', 'banana', 'cherry']
first = fruits[0]      # 'apple'
second = fruits[1]     # 'banana'
last = fruits[-1]      # 'cherry' (negative indexing)
```

## **3. List Length**
```python
colors = ['red', 'green', 'blue']
length = len(colors)   # 3

empty_list = []
empty_length = len(empty_list)  # 0
```

## **4. Appending to a List**
```python
numbers = [1, 2, 3]
numbers.append(4)      # [1, 2, 3, 4]
numbers.append('five') # [1, 2, 3, 4, 'five']
```

## **5. Removing from a List**
```python
animals = ['cat', 'dog', 'bird', 'cat']
animals.remove('cat')    # Removes first 'cat': ['dog', 'bird', 'cat']
animals.remove('bird')   # ['dog', 'cat']
```

## **6. Slicing a List**
```python
letters = ['a', 'b', 'c', 'd', 'e']
first_three = letters[0:3]    # ['a', 'b', 'c']
middle = letters[1:4]         # ['b', 'c', 'd']
last_two = letters[-2:]       # ['d', 'e']
all_copy = letters[:]         # ['a', 'b', 'c', 'd', 'e']
```

## **7. Concatenating Lists**
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2      # [1, 2, 3, 4, 5, 6]

names = ['alice']
new_names = names + ['bob', 'carol']  # ['alice', 'bob', 'carol']
```

## **8. Sorting a List**
```python
numbers = [3, 1, 4, 1, 5]
numbers.sort()               # [1, 1, 3, 4, 5]

words = ['zebra', 'apple', 'banana']
words.sort()                 # ['apple', 'banana', 'zebra']

# Reverse order
numbers.sort(reverse=True)   # [5, 4, 3, 1, 1]
```

## **9. Checking for an Element**

### **Single item checking:**
```python
fruits = ['apple', 'banana', 'cherry']
has_apple = 'apple' in fruits      # True
has_grape = 'grape' in fruits      # False
no_grape = 'grape' not in fruits   # True

# With numbers
numbers = [1, 2, 3, 4, 5]
has_three = 3 in numbers           # True
has_ten = 10 in numbers            # False
```

### **What are sets?**
```python
# Sets are like lists but with no duplicates and faster searching
fruits_list = ['apple', 'banana', 'apple']  # List can have duplicates
fruits_set = {'apple', 'banana'}            # Set removes duplicates

# Convert list to set
fruits_set = set(['apple', 'banana', 'apple'])  # Result: {'apple', 'banana'}
```

### **Multiple items checking (array of items):**
```python
fruits = ['apple', 'banana', 'cherry', 'date']
check_items = ['apple', 'grape', 'banana']

# Check if ALL items exist in fruits
all_exist = all(item in fruits for item in check_items)  # False (grape missing)

# Check if ANY items exist in fruits  
any_exist = any(item in fruits for item in check_items)  # True (apple, banana exist)

# Check if NONE of the items exist in fruits (clearer way)
none_exist = not any(item in fruits for item in check_items)  # False (some DO exist)
# Alternative way that feels less backwards:
# none_exist = all(item not in fruits for item in check_items)  # Same result

# Find which items exist
existing = [item for item in check_items if item in fruits]      # ['apple', 'banana']

# Find which items are missing
missing = [item for item in check_items if item not in fruits]   # ['grape']
```

### **Set operations (faster for large lists):**
```python
fruits = ['apple', 'banana', 'cherry', 'date']
check_items = ['apple', 'grape', 'banana']

fruits_set = set(fruits)
check_set = set(check_items)

# Items that exist in both
common = fruits_set & check_set           # {'apple', 'banana'}

# Items that are missing from fruits
missing = check_set - fruits_set          # {'grape'}

# Check if all items exist (using sets)
all_exist = check_set.issubset(fruits_set)  # False
```

## **Complete Example Using Multiple Operations**
```python
# Create a shopping list
shopping = ['milk', 'bread', 'eggs']

# Add items
shopping.append('butter')
shopping.append('cheese')

# Check what we have
print(f"List length: {len(shopping)}")
print(f"First item: {shopping[0]}")

# Remove an item
shopping.remove('bread')

# Check if item exists
if 'milk' in shopping:
    print("Don't forget the milk!")

# Get first 3 items
priority_items = shopping[:3]

# Sort the list
shopping.sort()
print(f"Sorted list: {shopping}")
``` 