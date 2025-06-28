# Advanced Parameters vs Global Variables

## **The Fundamental Design Question**

When should functions use **global variables** vs **parameters**? This is one of the most important design decisions in DevOps automation because it affects testability, reusability, and maintainability of your scripts.

**The Core Trade-off:**
- **Global variables**: Convenience vs Flexibility
- **Parameters**: Explicitness vs Verbosity

## **Global Variables Approach - When They Work Well**

### **Configuration That Rarely Changes:**

```python
# File: config/settings.py
"""Application-wide configuration - good use of global variables"""
DATABASE_URL = "postgresql://prod-db:5432/app"
API_KEY = "secret-api-key-123"
LOG_LEVEL = "INFO"
MAX_RETRY_ATTEMPTS = 3
TIMEOUT_SECONDS = 30

# File: database/connection.py
from config.settings import DATABASE_URL, MAX_RETRY_ATTEMPTS, TIMEOUT_SECONDS

def connect_to_database():
    """Connect using global configuration - appropriate here"""
    attempt = 0
    while attempt < MAX_RETRY_ATTEMPTS:  # Global: retry policy
        try:
            print(f"Connecting to: {DATABASE_URL}")  # Global: connection string
            connection = create_connection(DATABASE_URL, timeout=TIMEOUT_SECONDS)
            return connection
        except Exception as e:
            attempt += 1
            if attempt < MAX_RETRY_ATTEMPTS:
                time.sleep(2)
    raise Exception("Failed to connect after all attempts")

def get_user_count():
    """Uses global DB config - clean interface"""
    connection = connect_to_database()  # Uses global config internally
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    return cursor.fetchone()[0]

# Usage - Clean and simple
user_count = get_user_count()  # No parameters needed
```

**Why globals work well here:**
- Configuration is stable during execution
- Many functions need the same config
- Simplifies function interfaces
- Application-wide settings

## **Parameters Approach - When They Work Better**

### **Data That Changes Between Calls:**

```python
def process_server_logs(log_file, server_name=None, error_threshold=10):
    """Process logs with parameters - flexible and reusable"""
    error_count = 0
    actual_server = server_name or extract_server_name(log_file)
    
    for line in read_log_file(log_file):
        if "ERROR" in line:
            error_count += 1
    
    return {
        "server": actual_server,
        "errors": error_count,
        "alert_needed": error_count > error_threshold
    }

def analyze_server_health(server_results, critical_threshold=5):
    """Analyze with configurable thresholds"""
    total_errors = sum(result["errors"] for result in server_results)
    
    if total_errors > critical_threshold:
        return {"status": "critical", "total_errors": total_errors}
    else:
        return {"status": "healthy", "total_errors": total_errors}

# Usage - Flexible for different scenarios
web_results = []
for log_file in ["web-01.log", "web-02.log"]:
    # Web servers have higher error tolerance
    result = process_server_logs(log_file, error_threshold=20)
    web_results.append(result)

db_results = []
for log_file in ["db-01.log"]:
    # Database servers have lower error tolerance  
    result = process_server_logs(log_file, error_threshold=5)
    db_results.append(result)

# Different analysis for different server types
web_health = analyze_server_health(web_results, critical_threshold=15)
db_health = analyze_server_health(db_results, critical_threshold=8)
```

**Why parameters work well here:**
- Thresholds vary by server type
- Functions are reusable for different scenarios
- Easy to test with different values
- Can process multiple configurations simultaneously

## **Testing Comparison**

### **Testing with Global Variables (Harder):**

```python
# Global variables make testing difficult
DATABASE_URL = "postgresql://prod-db:5432/app"
ERROR_THRESHOLD = 10

def check_server_status():
    """Uses global variables - hard to test"""
    connection = connect_to_database()  # Uses global DATABASE_URL
    error_count = get_error_count(connection)
    return error_count > ERROR_THRESHOLD  # Uses global threshold

# Testing requires modifying globals
def test_check_server_status():
    global DATABASE_URL, ERROR_THRESHOLD
    
    # Have to change globals for testing
    original_db = DATABASE_URL
    original_threshold = ERROR_THRESHOLD
    
    try:
        DATABASE_URL = "postgresql://test-db:5432/test"
        ERROR_THRESHOLD = 5
        
        result = check_server_status()
        assert result == True
        
    finally:
        # Must restore globals
        DATABASE_URL = original_db
        ERROR_THRESHOLD = original_threshold
```

### **Testing with Parameters (Easier):**

```python
def check_server_status(database_url, error_threshold=10):
    """Uses parameters - easy to test"""
    connection = connect_to_database(database_url)
    error_count = get_error_count(connection)
    return error_count > error_threshold

# Testing is straightforward
def test_check_server_status():
    # Pass test values directly
    result = check_server_status(
        database_url="postgresql://test-db:5432/test",
        error_threshold=5
    )
    assert result == True
    
    # Test different scenarios easily
    result2 = check_server_status(
        database_url="postgresql://test-db:5432/test", 
        error_threshold=50
    )
    assert result2 == False
```

## **Mixed Approach - Best of Both Worlds**

### **Global Config + Operational Parameters:**

```python
# File: config/deployment_config.py
"""Global configuration for stable settings"""
DEPLOYMENT_ENVIRONMENTS = {
    "dev": {"replicas": 1, "cpu": "100m", "memory": "256Mi"},
    "staging": {"replicas": 2, "cpu": "500m", "memory": "512Mi"},
    "production": {"replicas": 3, "cpu": "1000m", "memory": "1Gi"}
}

DEFAULT_CONFIG = {
    "namespace": "default",
    "restart_policy": "Always"
}

# File: deployment/manager.py
from config.deployment_config import DEPLOYMENT_ENVIRONMENTS, DEFAULT_CONFIG

def deploy_application(app_name, environment, version, custom_config=None):
    """Mixed approach: global config + operational parameters"""
    
    # Use global configuration for environment defaults
    env_config = DEPLOYMENT_ENVIRONMENTS.get(environment)
    base_config = DEFAULT_CONFIG.copy()
    
    # Parameters provide the variable data
    deployment_config = {
        **base_config,           # Global stable config
        **env_config,            # Global environment config
        "app_name": app_name,    # Parameter - varies per deployment
        "version": version,      # Parameter - varies per deployment  
        **(custom_config or {})  # Parameter - specific overrides
    }
    
    print(f"Deploying {app_name} v{version} to {environment}")
    print(f"Replicas: {deployment_config['replicas']}")
    
    return create_k8s_deployment(deployment_config)

# Usage combines global and parameter benefits
deploy_application("web-api", "production", "v1.2.0")  # Uses global prod config

# Custom override via parameters when needed
deploy_application(
    "payment-api", 
    "production", 
    "v2.0.0",
    custom_config={"replicas": 5, "cpu": "2000m"}  # Override for critical service
)
```

## **Decision Framework**

### **Use Global Variables When:**
- Application-wide configuration (database URLs, API keys)
- Constants that never change (file size limits, timeouts)
- Expensive-to-compute values used everywhere
- Settings that all functions should share

### **Use Parameters When:**
- Data that varies between function calls
- Values needed for testing flexibility
- Configuration that changes based on context
- Dependencies that might be mocked

### **Red Flags:**
```python
# BAD: Global variables for operational data
current_deployment_status = {}  # Should be parameters/return values
last_processed_file = None      # Should be parameters/return values

# BAD: Too many parameters for stable config
def connect_db(host, port, user, password, database, pool_size, timeout, ssl_mode):
    pass  # This should use global config

# BAD: Functions that can't be called twice safely
def process_logs():
    global processed_count
    processed_count = 0  # Resets global state - problematic
```

## **Refactoring Examples**

### **From Global to Parameters (More Flexible):**

```python
# BEFORE: Hard to test
log_level = "INFO"
def format_log(message):
    if log_level == "DEBUG":
        return f"[DEBUG] {message}"
    return message

# AFTER: Flexible and testable
def format_log(message, log_level="INFO"):
    if log_level == "DEBUG":
        return f"[DEBUG] {message}"
    return message

# Still convenient with global default
LOG_LEVEL = "INFO"
def log_message(message):
    return format_log(message, LOG_LEVEL)
```

### **From Parameters to Global (Cleaner Interface):**

```python
# BEFORE: Repetitive parameters
def deploy(app, host, port, user, key_path, timeout, retries):
    pass

def health_check(host, port, user, key_path, timeout, endpoint):
    pass

# AFTER: Global config + operational params
SERVER_CONFIG = {
    "user": "deploy",
    "key_path": "/etc/keys/deploy",
    "timeout": 60,
    "retries": 3
}

def deploy(app_name, server_host, app_version):
    # Only operational data as parameters
    return perform_deploy(app_name, server_host, app_version, **SERVER_CONFIG)
```

## **Summary**

**Key Principles:**
✅ **Global Variables**: Use for stable configuration and shared application state  
✅ **Parameters**: Use for operational data and testing flexibility  
✅ **Mixed Approach**: Global config + operational parameters = optimal design  
✅ **Context Matters**: Same data might be global in one context, parameter in another  

**The Art of Balance**: Great DevOps automation uses globals for what should be stable and parameters for what should be flexible. The goal is code that's both convenient to use and powerful to customize.

Understanding when to use each approach helps you write automation that's easier to test, maintain, and adapt! 🚀 