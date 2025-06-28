# Parameters vs Global Variables

**1. What are parameters:**
Values passed into functions when you call them.

**2. Global variables approach:**
Function uses variables from outside itself.

```python
# Global variable approach
DATABASE_URL = "postgresql://localhost:5432/app"

def connect_database():
    print(f"Connecting to: {DATABASE_URL}")  # Uses global variable
    
connect_database()
```

**3. Parameters approach:**
Function receives values as inputs.

```python
# Parameters approach
def connect_database(database_url):
    print(f"Connecting to: {database_url}")  # Uses parameter
    
DATABASE_URL = "postgresql://localhost:5432/app"
connect_database(DATABASE_URL)  # Pass as parameter
```

**4. When to use global variables:**
- Configuration that rarely changes
- Values used by many functions
- Application-wide settings

**5. When to use parameters:**
- Data that changes between function calls
- Values specific to each operation
- When testing functions with different inputs

**6. Key difference:**
- Global: Function "knows" about outside variables
- Parameters: Function only knows what you give it 