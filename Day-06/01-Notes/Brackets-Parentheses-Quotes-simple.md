# Brackets, Parentheses, and Quotes - Simple

## Introduction

Quick reference for different bracket types and quotes in Python.

## Brackets `[ ]` - Lists and Indexing

### Creating Lists
```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
empty_list = []
```

### Accessing Elements
```python
servers = ["web-01", "web-02", "db-01"]
first_server = servers[0]    # "web-01"
last_server = servers[-1]    # "db-01"
```

### Slicing
```python
letters = ["a", "b", "c", "d", "e"]
first_three = letters[0:3]   # ["a", "b", "c"]
```

## Parentheses `( )` - Functions and Tuples

### Function Calls
```python
print("hello")
len([1, 2, 3])
max(5, 10, 3)
```

### Tuples
```python
coordinates = (3, 4)
servers = ("web", "db", "cache")
single_item = ("hello",)  # Note the comma
```

### Grouping Operations
```python
result = (5 + 3) * 2    # 16, not 11
```

## Curly Braces `{ }` - Dictionaries and Sets

### Dictionaries
```python
person = {"name": "John", "age": 30}
config = {"host": "localhost", "port": 8080}
```

### Sets
```python
unique_numbers = {1, 2, 3, 4, 5}
server_types = {"web", "database", "cache"}
```

### F-strings
```python
name = "Alice"
message = f"Hello {name}"
server = "web-01"
status = f"Server {server} is running"
```

## Quotes - Strings

### Single Quotes `' '`
```python
message = 'Hello World'
file_name = 'config.txt'
```

### Double Quotes `" "`
```python
greeting = "Welcome to Python"
path = "C:\Users\Documents"
```

### Triple Quotes `''' '''` or `""" """`
```python
long_text = """This is a
multi-line
string"""

documentation = '''
This function does something important.
It takes two parameters.
'''
```

## When to Use Which

### Brackets `[ ]`
- Lists of items
- Accessing elements by position
- Slicing sequences

### Parentheses `( )`
- Calling functions
- Creating tuples
- Grouping math operations
- Function parameters

### Curly Braces `{ }`
- Dictionaries (key-value pairs)
- Sets (unique items)
- F-string variables

### Quotes
- **Single quotes**: Simple strings
- **Double quotes**: Strings with apostrophes
- **Triple quotes**: Multi-line text

## Quick Examples

```python
# All together
servers = ["web-01", "web-02"]           # List with brackets
config = {"host": "localhost"}           # Dict with curly braces
coordinates = (10, 20)                   # Tuple with parentheses
message = f"Server {servers[0]} ready"   # F-string with curly braces

# Function call with all types
print(f"Config: {config}")               # Function() with f-string{}
``` 