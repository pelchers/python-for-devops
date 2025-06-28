# Parameters vs Global Variables

**1. What are parameters:**
Values passed into functions when you call them.

**2. Empty parentheses means no parameters:**
```python
def connect_database():  # Empty () = no parameters
    # This function will use global variables if it needs any data
    pass
```

**3. Global variables approach:**
Function uses variables from outside itself.

```python
# Global variable approach
DATABASE_URL = "postgresql://localhost:5432/app"

def connect_database():  # No parameters needed
    print(f"Connecting to: {DATABASE_URL}")  # Uses global variable
    
connect_database()  # No values passed
```

**4. Parameters approach:**
Function receives values as inputs.

```python
# Parameters approach
def connect_database(database_url):  # Has parameter
    print(f"Connecting to: {database_url}")  # Uses parameter
    
DATABASE_URL = "postgresql://localhost:5432/app"
connect_database(DATABASE_URL)  # Pass value as parameter
```

**5. Parameter defaults:**
```python
def connect_database(database_url="default://localhost"):  # Default value
    print(f"Connecting to: {database_url}")

connect_database()  # Uses default
connect_database("custom://server")  # Uses provided value
```

**6. Different sources of variables (instead of parameters):**

```python
# From other files (imported globals)
from config import DATABASE_URL  # Outside file global

# In this file (file globals)  
ERROR_THRESHOLD = 10             # In-file global
APP_NAME = "MyApp"              # In-file global

def process_data():
    # Inside function (local variables)
    temp_count = 0              # Local variable instead of parameter
    
    # Function can use any of these instead of parameters:
    print(DATABASE_URL)         # Uses imported global
    print(ERROR_THRESHOLD)      # Uses file global  
    print(APP_NAME)            # Uses file global
    print(temp_count)          # Uses local variable
```

**7. How Python finds variables:**
- First looks for local variables (parameters, variables inside function)
- Then looks for global variables (variables outside function)
- If not found anywhere, gives error

**7. When to use global variables:**
- Configuration that rarely changes
- Values used by many functions
- Application-wide settings

**8. When to use parameters:**
- Data that changes between function calls
- Values specific to each operation
- When testing functions with different inputs

**9. Why not just use globals for everything?**

**Problem with only globals:**
```python
# Trying to use only globals - THIS BREAKS!
server_name = "web-01"
error_threshold = 10

def process_server():
    print(f"Processing {server_name} with threshold {error_threshold}")
    # Process the server...

# This works fine for one server:
process_server()  # Processes web-01

# But what if you need to process multiple servers?
server_name = "web-02"  # Change global
process_server()        # Now processes web-02

server_name = "db-01"   # Change global again  
process_server()        # Now processes db-01

# PROBLEM: Can only process ONE server at a time!
# PROBLEM: Have to keep changing globals!
# PROBLEM: Easy to forget which server you're processing!
```

**Solution with parameters:**
```python
def process_server(server_name, error_threshold):
    print(f"Processing {server_name} with threshold {error_threshold}")
    # Process the server...

# Now you can process multiple servers easily:
process_server("web-01", 10)
process_server("web-02", 10)  
process_server("db-01", 5)

# Can even process different servers with different settings:
process_server("web-01", 20)    # Web server, high threshold
process_server("db-01", 5)      # Database server, low threshold
```

**10. Key difference:**
- Global: Function "knows" about outside variables
- Parameters: Function only knows what you give it

**11. The key insight - Single vs Multiple:**

**Single value = Use globals:**
```python
# Only ONE database URL for the whole app
DATABASE_URL = "postgresql://prod-db:5432/app"  # Global - only one value

def connect_to_database():
    print(f"Connecting to {DATABASE_URL}")  # Uses global - always the same
```

**Multiple values = Use parameters:**
```python
# Multiple users from database - need parameters!
def process_user(username, email, role):
    print(f"Processing user {username} ({email}) with role {role}")

# Get multiple users from database
users = [
    ("alice", "alice@company.com", "admin"),
    ("bob", "bob@company.com", "user"), 
    ("carol", "carol@company.com", "manager")
]

# Process each user - different data each time
for username, email, role in users:
    process_user(username, email, role)  # Parameters needed!
```

**Multiple servers = Use parameters:**
```python
# Multiple servers from servers file - need parameters!
servers = [
    {"name": "web-01", "ip": "192.168.1.10", "type": "web"},
    {"name": "web-02", "ip": "192.168.1.11", "type": "web"},
    {"name": "db-01", "ip": "192.168.1.20", "type": "database"}
]

def monitor_server(server_name, server_ip, server_type):
    print(f"Monitoring {server_type} server {server_name} at {server_ip}")

# Monitor each server - different data each time  
for server in servers:
    monitor_server(server["name"], server["ip"], server["type"])  # Parameters needed!
```

**12. When parameters are essential:**
- Processing different data each time
- Using same function for multiple things
- Testing with different values
- Running multiple operations simultaneously 