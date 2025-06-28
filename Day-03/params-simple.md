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

**9. Key difference:**
- Global: Function "knows" about outside variables
- Parameters: Function only knows what you give it 