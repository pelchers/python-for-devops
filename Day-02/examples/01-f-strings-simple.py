# Basic f-string examples
name = "Alice"
age = 30
score = 95.7

# Simple variable insertion
message = f"Hello {name}"
print(message)

# Multiple variables
info = f"{name} is {age} years old"
print(info)

# Expressions inside f-strings
status = f"Score: {score:.1f}% ({'Pass' if score >= 60 else 'Fail'})"
print(status)

# Math expressions
total = f"Total: {age + score}"
print(total) 