# Variables - Scope and Lifetime

**1. Variable Scope:**
Where in your code a variable can be accessed.

**2. Local Scope:**
Variables created inside functions can only be used inside that function.

```python
def check_server():
    server_name = "web-01"  # Local variable
    print(server_name)      # Works here

check_server()
# print(server_name)        # Error - can't access outside function
```

**3. Global Scope:**
Variables created outside functions can be used anywhere in the code.

```python
environment = "production"  # Global variable

def deploy_app():
    print(environment)      # Can access global variable

deploy_app()                # Prints: production
print(environment)          # Also works here
```

**4. Variable Lifetime:**
- Local variables: Created when function runs, destroyed when function ends
- Global variables: Created when program starts, destroyed when program ends

**5. Cross-File Global Variables:**
Variables shared between multiple Python files using imports.

```python
# config.py file
DATABASE_URL = "postgresql://localhost:5432/app"
API_KEY = "secret-key-123"

# main.py file
from config import DATABASE_URL, API_KEY

def connect_database():
    print(f"Connecting to: {DATABASE_URL}")
    print(f"Using API key: {API_KEY}")
```

**6. Repository-Wide Global Variables:**
Variables shared across entire project using environment variables.

```python
import os

# Read from environment variables
DATABASE_URL = os.getenv("DATABASE_URL", "localhost:5432")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

def deploy_app():
    print(f"Deploying to: {ENVIRONMENT}")
    print(f"Database: {DATABASE_URL}")
``` 