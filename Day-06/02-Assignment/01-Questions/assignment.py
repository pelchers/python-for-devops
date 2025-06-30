# Flask web server code (commented out for assignment work)
# from flask import Flask
# 
# app = Flask(__name__)
# 
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'
# 
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=8000)

print("task 1")

a=1
b=2
print("Hello World!")

def add(a,b):
    return a+b

print(add(a,b))

result = add(a,b)
print(result)

print("task 2")

print(a>b) 
print(a<b)

print("task 3")

x = True
y = False

print (x and y)
print (x or y)
print (not x, not y)

print("task 4")

total = 10

print(total)

total += 10

print(total)

total -= 5

print(total)

total *= 2

print("task 5")

print("bitwise operators are rarely used in python! we can do this later... thank you!")



print("task 6")

# 1. Create a list my_list containing a few elements
my_list = [1, 2, 3, "hello", "world"]

# 2. Use identity operators (is and is not) to check if two variables are the same object
list_a = my_list
list_b = [1, 2, 3, "hello", "world"]  # Different object, same content

print("Identity operators:")
print(f"list_a is my_list: {list_a is my_list}")           # True - same object
print(f"list_b is my_list: {list_b is my_list}")           # False - different object
print(f"list_a is not list_b: {list_a is not list_b}")     # True - different objects

# 3. Use membership operators (in and not in) to check if element is present in my_list
print("Membership operators:")
print(f"1 in my_list: {1 in my_list}")                     # True
print(f"'hello' in my_list: {'hello' in my_list}")         # True
print(f"99 in my_list: {99 in my_list}")                   # False
print(f"99 not in my_list: {99 not in my_list}")           # True
print(f"'goodbye' not in my_list: {'goodbye' not in my_list}")  # True

# Additional examples with the nested structures from above
print("Additional identity checks with nested data:")
print(f"p[1] is q[1]: {p[1] is q[1]}")                     # False - different tuples
print(f"p[1][2] is q[1][2]: {p[1][2] is q[1][2]}")         # Depends on Python's integer caching

print("this is slignjtly different from the above, but it's the same concept")
print(p[1] is q[1])
print (p[1][2] is q[1][2]) 





print("tuple testing")

# List variation
x = [1,2,3,4,5]
y = [4,5,6,7,8]
z = [7,8,9,10,11]

my_list = [x,y,z]

print("my_list is a LIST containing lists:")
print(my_list[0]) # [1, 2, 3, 4, 5]
print(my_list[1]) # [4, 5, 6, 7, 8]
print(my_list[2]) # [7, 8, 9, 10, 11]

# Complicated list variation (mimicking database-like results)
# ❌ WRONG: Can't use assignments inside list literals
# u = [
#     d = [1,2,3,4,5],
#     e = [6,7,8,9,10],
#     f = [11,12,13,14,15]
# ]

# ✅ CORRECT: Create nested lists directly
u = [
    [1,2,3,4,5],      # Row 1
    [6,7,8,9,10],     # Row 2  
    [11,12,13,14,15]  # Row 3
]

v = [
    [16,17,18,19,20],
    [21,22,23,24,25],
    [26,27,28,29,30]
]

w = [
    [31,32,33,34,35],
    [36,37,38,39,40],
    [41,42,43,44,45]
]

my_complicated_list = [u,v,w]
print("Complicated list (mutable - can change):")
print(my_complicated_list[0][0])  # First row of first group: [1,2,3,4,5]
# Note: Lists can be modified after creation, unlike database results



# Tuple variation
a = (1,2,3,4,5)
b = (4,5,6,7,8)
c = (7,8,9,10,11)

my_tuple_list = [a,b,c]

print("my_tuple_list is a LIST containing tuples:")
print(my_tuple_list[0]) # (1, 2, 3, 4, 5)
print(my_tuple_list[1]) # (4, 5, 6, 7, 8)
print(my_tuple_list[2]) # (7, 8, 9, 10, 11)

# Complicated tuple variation (like real database results)
# Database results are typically tuples because they're immutable
p = (
    (1,2,3,4,5),      # Row 1 - immutable
    (6,7,8,9,10),     # Row 2 - immutable
    (11,12,13,14,15)  # Row 3 - immutable  
)

q = (
    (16,17,18,19,20),
    (21,22,23,24,25),
    (26,27,28,29,30)
)

r = (
    (31,32,33,34,35),
    (36,37,38,39,40),
    (41,42,43,44,45)
)

my_complicated_tuples = [p,q,r]
print("Complicated tuples (immutable - like database results):")
print(my_complicated_tuples[0][0])  # First row of first group: (1,2,3,4,5)
# Note: Tuples cannot be modified after creation, just like database results