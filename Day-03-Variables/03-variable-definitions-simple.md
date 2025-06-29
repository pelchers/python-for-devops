# Variable Definitions - 4 Ways to Create Variables

---
## **⚡ WHEN CONFUSED - READ THIS FIRST! ⚡**
**Simple = Just type it | Complex = Lists/tuples | External = From files/databases | Import = From other files**
---

**1. Simple variables (just type them):**
```python
# Just assign a value directly
server_name = "web-01"
port = 80
is_active = True
```

**2. Complex variables (lists, tuples, dictionaries):**
```python
# Multiple values in one variable
servers = ["web-01", "web-02", "db-01"]              # List named 'servers' contains server names
user_info = ("Alice", "admin", "alice@co.com")       # Tuple named 'user_info' contains user data
config = {"host": "localhost", "port": 5432}         # Dictionary named 'config' contains settings

# HOW DO WE KNOW WHAT EACH ITEM REPRESENTS?

# FOR LISTS - Position doesn't matter, but you need to document what type of data:
servers = ["web-01", "web-02", "db-01"]              # All items are SERVER NAMES
ip_addresses = ["192.168.1.10", "192.168.1.11"]     # All items are IP ADDRESSES  
ports = [80, 443, 8080]                              # All items are PORT NUMBERS

# FOR TUPLES - Position MATTERS, you decide what each position means:
user_info = ("Alice", "admin", "alice@co.com")       # Position 0=name, Position 1=role, Position 2=email
server_info = ("web-01", "192.168.1.10", 80)        # Position 0=name, Position 1=ip, Position 2=port

# YOU DECIDE THE ORDER when creating tuples:
# ("Alice", "admin", "alice@co.com") = name first, role second, email third
# ("admin", "Alice", "alice@co.com") = role first, name second, email third (different order!)

# WHEN YOU UNPACK, ORDER MUST MATCH:
name, role, email = user_info                        # Must match tuple order: name, role, email
# role, name, email = user_info                      # WRONG! Doesn't match tuple order

# WHERE NAMES COME FROM:
# servers = the variable name (you choose this)
# ["web-01", "web-02", "db-01"] = the actual server names inside the list
# "web-01" = first server name, "web-02" = second server name, etc.
```

**3. External variables (from files, databases, APIs):**
```python
# Get data from outside sources
import json
users = json.load(open("users.json"))                # Variable 'users' gets data from "users.json" file
servers = cursor.fetchall()                          # Variable 'servers' gets data from database query
response = requests.get("http://api.com/servers")    # Variable 'response' gets data from API call
server_list = response.json()                        # Variable 'server_list' converts response to Python data

# WHERE EXTERNAL DATA COMES FROM:
# "users.json" = the filename (file must exist)
# users = variable name for the file data (you choose this)
# cursor.fetchall() = gets results from a database query 
# servers = variable name for the database results (you choose this)
# "http://api.com/servers" = the API URL (external website)
# response = variable name for the API response (you choose this)
```

**4. Import variables (from other files):**
```python
# Get variables defined in other files
from config import DATABASE_URL, API_KEY             # Get 2 variables from config.py file
from servers import PRODUCTION_SERVERS               # Get 1 variable from servers.py file

# WHERE IMPORT VARIABLES COME FROM:
# config = the filename (config.py file must exist)
# DATABASE_URL, API_KEY = variable names defined in config.py (defined there)
# servers = the filename (servers.py file must exist)  
# PRODUCTION_SERVERS = variable name defined in servers.py (defined there)
# Now you can use DATABASE_URL, API_KEY, PRODUCTION_SERVERS in this file
```

**5. How to use each type:**
```python
# Simple - use directly
print(f"Server: {server_name}")  # server_name is the variable you defined above

# Complex - loop through or access parts
for server in servers:  # 'server' gets each name from the 'servers' list
    print(f"Processing {server}")  # server = "web-01", then "web-02", then "db-01"

# For tuples in loops, unpacking order must match:
user_data = [("Alice", "admin"), ("Bob", "user")]    # Position 0=name, Position 1=role
for name, role in user_data:  # Must unpack in same order: name first, role second
    print(f"{name} is {role}")  # name="Alice", role="admin", then name="Bob", role="user"

# HOW FUNCTIONS KNOW WHAT EACH PARAMETER MEANS:
def setup_user(username, user_role):  # Function expects: position 0=username, position 1=user_role
    print(f"Setting up {username} as {user_role}")

# When calling with unpacked tuple:
for name, role in user_data:
    setup_user(name, role)  # name goes to username, role goes to user_role (BY ORDER!)

# THE FUNCTION DOESN'T KNOW ABOUT YOUR TUPLE STRUCTURE OR WHICH VARIABLE YOU USE!
# Function just receives: setup_user("Alice", "admin")
# It doesn't know these came from a tuple ("Alice", "admin") or from user_data variable
# Order must match: tuple position 0 → function parameter 0, tuple position 1 → function parameter 1

# 🔥 THE FUNCTION DOESN'T KNOW WHICH VARIABLE YOU CHOOSE TO USE! 🔥
# You might have multiple variables with same 3-item structure:
users = [("john", "admin", "john@company.com"), ("sarah", "user", "sarah@company.com")]
functions = [("backup", "daily", "backup@system.com"), ("monitor", "hourly", "monitor@system.com")]
servers = [("web-01", "active", "web-01@system.com"), ("db-01", "standby", "db-01@system.com")]

def create_user_account(username, user_role, email_address):
    print(f"Creating account for {username} ({user_role}) - Email: {email_address}")

# YOU choose which variable to use - function doesn't know or care:

# Choice 1: Use the users variable (makes sense)
print("Using USERS variable:")
for user in users:
    create_user_account(user[0], user[1], user[2])
    # Function receives: ("john", "admin", "john@company.com")
    # Function doesn't know this came from 'users' variable

# Choice 2: Use the functions variable (works but makes no sense!)
print("\nUsing FUNCTIONS variable (bad idea but works):")
for func in functions:
    create_user_account(func[0], func[1], func[2])
    # Function receives: ("backup", "daily", "backup@system.com")
    # Function doesn't know this came from 'functions' variable
    # Result: "Creating account for backup (daily) - Email: backup@system.com"

# Choice 3: Use the servers variable (also works but wrong!)
print("\nUsing SERVERS variable (bad idea but works):")
for server in servers:
    create_user_account(server[0], server[1], server[2])
    # Function receives: ("web-01", "active", "web-01@system.com")
    # Function doesn't know this came from 'servers' variable
    # Result: "Creating account for web-01 (active) - Email: web-01@system.com"

# 🔥 KEY INSIGHT: The function just gets the VALUES, not the variable names!
# create_user_account("john", "admin", "john@company.com") ← function only sees this
# It doesn't know if the values came from users[0] or functions[0] or servers[0]
# YOU decide which variable to use based on what makes sense for your task!

# ⚡⚡⚡ BREAKTHROUGH UNDERSTANDING: UNPACKING IS WHERE YOU DECIDE! ⚡⚡⚡
# 
# UNPACKING = Where YOU choose which variable and its tuples the function gets!
#
# for user in users:                    ← YOU chose 'users' variable here!
#     create_user_account(user[0], user[1], user[2])  ← Unpacking users tuples
#
# for func in functions:                ← YOU chose 'functions' variable here!  
#     create_user_account(func[0], func[1], func[2])  ← Unpacking functions tuples
#
# The function doesn't know which variable you picked - YOU control it with unpacking!

# WRONG: Using a variable with different tuple structure!
server_data = [("web-01", "192.168.1.10", "web")]  # name, ip, type (3 items!)

# This would be WRONG:
# for name, role in server_data:  # Trying to unpack 3 items into 2 variables - ERROR!
#     setup_user(name, role)

# Only use variables that match your unpacking pattern!

# COMMON MISTAKE - WRONG ORDER:
server_data = ("192.168.1.10", "web-01", "web")     # ip, name, type

def setup_server(name, ip, type):  # Function expects: name, ip, type
    print(f"Server {name} at {ip} is {type}")

# WRONG WAY:
ip, name, type = server_data  # Unpack in tuple order
setup_server(ip, name, type)  # Pass in wrong order!
# Result: setup_server("192.168.1.10", "web-01", "web") 
# Function thinks: name="192.168.1.10", ip="web-01", type="web" - WRONG!

# RIGHT WAY:
ip, name, type = server_data  # Unpack in tuple order  
setup_server(name, ip, type)  # Reorder to match function!
# Result: setup_server("web-01", "192.168.1.10", "web")
# Function gets: name="web-01", ip="192.168.1.10", type="web" - CORRECT!

# WHERE LOOP NAMES COME FROM:
# servers = the list variable name (defined above)
# server = the loop variable name (you choose this, could be anything)
# server gets each value: first "web-01", then "web-02", then "db-01"
# 
# For tuples:
# user_data = the list variable name (you choose this)
# name, role = the unpacking variable names (you choose these, must match tuple order)

# External - same as complex once loaded
for user in users:  # 'user' gets each item from the 'users' list
    print(f"User: {user}")  # user = first user data, then second user data, etc.

# Import - use like simple variables  
connection = connect(DATABASE_URL)  # DATABASE_URL comes from the imported file
```

**6. When to use each:**
- **Simple**: Single values that don't change much
- **Complex**: Multiple related items you create yourself  
- **External**: Data that comes from outside your code
- **Import**: Configuration shared across multiple files

**7. Real-life beginner workflow example:**
```python
# Step 1: Beginner starts with simple variables (easiest)
server_name = "web-01"
server_ip = "192.168.1.10"

def check_server(name, ip):
    print(f"Checking {name} at {ip}")

# Test with simple variables
check_server(server_name, server_ip)  # Output: Checking web-01 at 192.168.1.10

# Step 2: Beginner realizes they need multiple servers (moves to lists)
servers = ["web-01", "web-02", "db-01"]  # All server names

def check_server_simple(name):
    print(f"Checking {name}")

# Test with list
for server in servers:  # server gets each name from servers list
    check_server_simple(server)  # Pass each server name

# Step 3: Beginner needs more info per server (moves to tuples)
server_info = [
    ("web-01", "192.168.1.10"),  # name, ip
    ("web-02", "192.168.1.11"),  # name, ip
    ("db-01", "192.168.1.20")    # name, ip
]

def check_server_detailed(name, ip):
    print(f"Checking {name} at {ip}")

# Test with tuples - unpacking happens in the loop
for name, ip in server_info:  # Unpack each tuple into name and ip
    check_server_detailed(name, ip)  # Pass unpacked values to function

# This is the natural learning progression: simple → lists → tuples
```

**8. Tuple workflow example:**
```python
# Beginner defines tuple structure first
print("=== Testing Tuple Workflow ===")

# Step 1: Define the tuple structure and document it
users = [
    ("Alice", "admin", "alice@company.com"),  # name, role, email
    ("Bob", "user", "bob@company.com"),       # name, role, email
    ("Carol", "manager", "carol@company.com") # name, role, email
]

# Step 2: Create function that expects the data in specific order
def create_user_account(username, user_role, email_address):
    print(f"Creating account for {username} ({user_role}) - Email: {email_address}")

# Step 3: Test with one tuple first (beginner approach)
first_user = users[0]  # Get first tuple: ("Alice", "admin", "alice@company.com")
name, role, email = first_user  # Unpack tuple into separate variables
create_user_account(name, role, email)  # Pass to function

# Step 4: When confident, loop through all tuples
print("\nCreating all user accounts:")
for name, role, email in users:  # Unpack each tuple in the loop
    create_user_account(name, role, email)  # Function gets individual values

# Step 5: Beginner realizes they can reorder if needed
print("\nTesting with different function parameter order:")

def setup_email(email_addr, full_name, access_level):  # Different parameter order!
    print(f"Setting up email {email_addr} for {full_name} with {access_level} access")

# Must reorder when calling function to match its parameter order
for name, role, email in users:  # Unpack in tuple order
    setup_email(email, name, role)  # Reorder to match function: email, name, role

# Key learning: Tuple order is fixed, but you can reorder when calling functions
``` 