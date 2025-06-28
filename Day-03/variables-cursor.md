# Advanced Variables - Scope and Lifetime

## **What is Variable Scope and Lifetime?**

Variable scope determines **where in your code a variable can be accessed**, while lifetime determines **when variables are created and destroyed**. Understanding these concepts is crucial for writing reliable DevOps automation scripts.

## **Local Scope Deep Dive**

### **Function-Level Variable Isolation:**

```python
def check_server_status():
    server_name = "web-01"          # Local variable
    status = "healthy"              # Local variable
    cpu_usage = 45                  # Local variable
    
    print(f"Server {server_name} is {status} (CPU: {cpu_usage}%)")
    return status

# Function creates its own isolated scope
result = check_server_status()
# Output: Server web-01 is healthy (CPU: 45%)

# These would cause NameError - variables don't exist outside function
# print(server_name)  # NameError: name 'server_name' is not defined
```

### **Why Local Scope Matters in DevOps:**

```python
def process_log_file(log_path):
    """Process a single log file - all variables are local"""
    error_count = 0                 # Local to this function
    warning_count = 0               # Local to this function
    processed_lines = 0             # Local to this function
    
    with open(log_path, 'r') as file:
        for line in file:           # 'line' is also local
            processed_lines += 1
            if "ERROR" in line:
                error_count += 1
            elif "WARNING" in line:
                warning_count += 1
    
    return {
        "errors": error_count,
        "warnings": warning_count, 
        "total_lines": processed_lines
    }
# All local variables destroyed when function ends
```

## **Global Scope Deep Dive**

### **Application-Wide Configuration:**

```python
# Global configuration variables (accessible everywhere)
APPLICATION_NAME = "web-api"
ENVIRONMENT = "production"
DATABASE_HOST = "prod-db.example.com"
DEBUG_MODE = False

def initialize_database():
    """Function can access global configuration"""
    print(f"Connecting to {DATABASE_HOST} for {APPLICATION_NAME}")
    print(f"Environment: {ENVIRONMENT}")
    # Uses global variables for configuration

def deploy_application():
    """Deployment function using global state"""
    if ENVIRONMENT == "production":
        replica_count = 3
    else:
        replica_count = 1
    
    print(f"Deploying {APPLICATION_NAME} with {replica_count} replicas")
    return replica_count

# All functions can access the global variables
initialize_database()    # Output: Connecting to prod-db.example.com for web-api
replicas = deploy_application()  # Output: Deploying web-api with 3 replicas
```

### **Modifying Global Variables:**

```python
# Global variables
SERVER_COUNT = 0
DEPLOYMENT_STATUS = "idle"

def update_global_state(new_count, new_status):
    """Function that modifies global variables"""
    global SERVER_COUNT, DEPLOYMENT_STATUS  # Need 'global' keyword to modify
    
    timestamp = "2024-01-01 10:05:00"  # Local variable
    
    # Modifying global variables
    SERVER_COUNT = new_count
    DEPLOYMENT_STATUS = new_status
    
    print(f"Global state updated at {timestamp}")
    print(f"New server count: {SERVER_COUNT}")

# Usage
update_global_state(5, "deploying")
# Output: Global state updated at 2024-01-01 10:05:00
# Output: New server count: 5
```

## **Variable Lifetime Examples**

### **Local Variable Lifecycle:**

```python
def demonstrate_local_lifetime():
    """Show when local variables are created and destroyed"""
    
    print("Function starts - no local variables exist yet")
    
    # Variables created here
    server_list = ["web-01", "web-02", "db-01"]  # Created now
    processed_count = 0                          # Created now
    
    print("Local variables created")
    
    for server in server_list:
        processed_count += 1
        print(f"Processing {server} (count: {processed_count})")
    
    print(f"Final count: {processed_count}")
    print("Function ending - all local variables about to be destroyed")
    
    return processed_count

result = demonstrate_local_lifetime()
print(f"Function finished. Result: {result}")
# All local variables from function are now destroyed
```

### **Global Variable Persistence:**

```python
# Global variables created when program starts
SYSTEM_START_TIME = "2024-01-01 09:00:00"
ACTIVE_CONNECTIONS = 0

def simulate_connection():
    """Demonstrate how global variables persist"""
    global ACTIVE_CONNECTIONS
    
    # Local variable
    event_time = "2024-01-01 09:15:00"
    
    # Modify global variable
    ACTIVE_CONNECTIONS += 1
    
    print(f"Connection at {event_time}")
    print(f"Total connections: {ACTIVE_CONNECTIONS}")
    # event_time destroyed when function ends
    # ACTIVE_CONNECTIONS persists

# Call multiple times - global state persists
simulate_connection()  # ACTIVE_CONNECTIONS = 1
simulate_connection()  # ACTIVE_CONNECTIONS = 2
simulate_connection()  # ACTIVE_CONNECTIONS = 3

print(f"System running since: {SYSTEM_START_TIME}")
print(f"Final connections: {ACTIVE_CONNECTIONS}")
```

## **Advanced Scope Patterns**

### **Nested Function Scope:**

```python
def create_server_monitor(server_name):
    """Outer function creates variables accessible to inner function"""
    start_time = "2024-01-01 10:00:00"  # Enclosing scope
    check_count = 0                      # Enclosing scope
    
    def check_health():
        """Inner function can access enclosing scope"""
        nonlocal check_count  # Can modify enclosing scope
        
        current_time = "2024-01-01 10:05:00"  # Local to inner function
        check_count += 1
        
        print(f"Health check #{check_count} for {server_name}")
        print(f"Started: {start_time}, Current: {current_time}")
        return "healthy"
    
    return check_health

# Create monitor functions
web_monitor = create_server_monitor("web-01")
db_monitor = create_server_monitor("db-01")

# Each maintains its own enclosing scope
web_monitor()  # check_count = 1 for web-01
web_monitor()  # check_count = 2 for web-01
db_monitor()   # check_count = 1 for db-01 (separate scope)
```

## **Common Scope Problems**

### **Accidental Global Modification:**

```python
# Global configuration
config = {"environment": "production"}

def bad_config_update(new_env):
    """BAD: Accidentally modifies global"""
    config["environment"] = new_env  # Modifies global!
    config["updated"] = True         # Adds to global!
    return config

def good_config_update(new_env):
    """GOOD: Creates local copy"""
    local_config = config.copy()     # Local copy
    local_config["environment"] = new_env
    local_config["updated"] = True
    return local_config

print("Original config:", config)

bad_result = bad_config_update("staging")
print("After bad update:", config)  # Global modified!

good_result = good_config_update("development") 
print("After good update:", config)  # Global unchanged
print("Good result:", good_result)
```

## **Best Practices**

### **1. Use Global for Configuration:**

```python
# Good: Global constants
DATABASE_URL = "postgresql://prod:5432/app"
LOG_LEVEL = "INFO"
MAX_RETRIES = 3

def connect_database():
    """Good: Use global config, local processing"""
    connection = None
    attempt = 0
    
    while attempt < MAX_RETRIES:  # Global constant
        try:
            connection = create_connection(DATABASE_URL)  # Global config
            break
        except Exception:
            attempt += 1  # Local counter
    
    return connection
```

### **2. Keep Local Scope Small:**

```python
def process_servers(server_list):
    """Good: Each operation has minimal scope"""
    results = []
    
    for server in server_list:
        # Local variables for each server
        start_time = get_current_time()
        success = False
        
        try:
            success = deploy_to_server(server)
            results.append({"server": server, "success": success, "time": start_time})
        except Exception as e:
            error_msg = f"Failed {server}: {e}"  # Local error handling
            results.append({"server": server, "success": False, "error": error_msg})
        
        # start_time, success, error_msg cleaned up each iteration
    
    return results
```

## **Summary**

Understanding variable scope and lifetime helps you:

✅ **Prevent variable conflicts** - Proper scope isolation  
✅ **Manage memory efficiently** - Local variables auto-cleanup  
✅ **Write maintainable code** - Clear variable access patterns  
✅ **Debug more easily** - Predictable variable behavior  
✅ **Handle configuration properly** - Global vs local usage  

**Key Rules:**
- **Local variables**: Created when needed, destroyed when function ends
- **Global variables**: Exist for entire program, use for configuration
- **Use `global` keyword**: When modifying global variables inside functions
- **Avoid global state**: Use local variables when possible

## **Cross-File Global Variables**

### **Module-Level Configuration Sharing:**

Variables can be shared across multiple files by importing them from configuration modules.

```python
# File: config/settings.py
"""Central configuration module for the application"""
DATABASE_URL = "postgresql://prod-db:5432/myapp"
REDIS_URL = "redis://cache:6379"
API_BASE_URL = "https://api.example.com"
LOG_LEVEL = "INFO"
MAX_RETRIES = 3
TIMEOUT_SECONDS = 30

# Environment-specific overrides
ENVIRONMENTS = {
    "development": {
        "DATABASE_URL": "postgresql://localhost:5432/myapp_dev",
        "LOG_LEVEL": "DEBUG"
    },
    "staging": {
        "DATABASE_URL": "postgresql://staging-db:5432/myapp",
        "LOG_LEVEL": "WARNING"
    },
    "production": {
        "DATABASE_URL": "postgresql://prod-db:5432/myapp",
        "LOG_LEVEL": "ERROR"
    }
}

def get_config(environment="production"):
    """Return configuration for specific environment"""
    base_config = {
        "DATABASE_URL": DATABASE_URL,
        "REDIS_URL": REDIS_URL,
        "API_BASE_URL": API_BASE_URL,
        "LOG_LEVEL": LOG_LEVEL,
        "MAX_RETRIES": MAX_RETRIES,
        "TIMEOUT_SECONDS": TIMEOUT_SECONDS
    }
    
    # Override with environment-specific settings
    if environment in ENVIRONMENTS:
        base_config.update(ENVIRONMENTS[environment])
    
    return base_config
```

### **Using Cross-File Variables in Different Modules:**

```python
# File: database/connection.py
"""Database connection module"""
from config.settings import DATABASE_URL, MAX_RETRIES, TIMEOUT_SECONDS
import time

def create_connection():
    """Create database connection using global config"""
    attempt = 0
    connection = None
    
    while attempt < MAX_RETRIES:  # Global variable from config
        try:
            print(f"Connecting to: {DATABASE_URL}")  # Global variable
            connection = connect_db(DATABASE_URL, timeout=TIMEOUT_SECONDS)
            print("Database connection successful")
            break
        except Exception as e:
            attempt += 1
            print(f"Connection attempt {attempt} failed: {e}")
            if attempt < MAX_RETRIES:
                time.sleep(2)
    
    return connection

# File: api/client.py 
"""API client module"""
from config.settings import API_BASE_URL, TIMEOUT_SECONDS, MAX_RETRIES

def make_api_request(endpoint, data=None):
    """Make API request using global configuration"""
    url = f"{API_BASE_URL}/{endpoint}"  # Global variable
    
    for attempt in range(MAX_RETRIES):  # Global variable
        try:
            response = requests.post(url, json=data, timeout=TIMEOUT_SECONDS)
            return response.json()
        except Exception as e:
            print(f"API request attempt {attempt + 1} failed: {e}")
            if attempt == MAX_RETRIES - 1:
                raise
    
# File: logging/setup.py
"""Logging configuration module"""
from config.settings import LOG_LEVEL
import logging

def setup_logging():
    """Configure logging using global settings"""
    numeric_level = getattr(logging, LOG_LEVEL.upper(), logging.INFO)
    logging.basicConfig(
        level=numeric_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    print(f"Logging configured at {LOG_LEVEL} level")
```

### **Dynamic Cross-File Configuration:**

```python
# File: config/dynamic.py
"""Dynamic configuration that can be updated at runtime"""
import threading

class GlobalConfig:
    """Thread-safe global configuration that can be modified"""
    
    def __init__(self):
        self._config = {
            "database_url": "postgresql://localhost:5432/app",
            "cache_enabled": True,
            "debug_mode": False,
            "max_workers": 4,
            "rate_limit": 100
        }
        self._lock = threading.Lock()
    
    def get(self, key, default=None):
        """Get configuration value"""
        with self._lock:
            return self._config.get(key, default)
    
    def set(self, key, value):
        """Set configuration value"""
        with self._lock:
            self._config[key] = value
            print(f"Global config updated: {key} = {value}")
    
    def update(self, new_config):
        """Update multiple configuration values"""
        with self._lock:
            self._config.update(new_config)
            print(f"Global config updated with: {new_config}")
    
    def get_all(self):
        """Get all configuration values"""
        with self._lock:
            return self._config.copy()

# Global instance shared across modules
global_config = GlobalConfig()

# File: workers/processor.py
"""Worker module using dynamic global config"""
from config.dynamic import global_config

def process_tasks():
    """Process tasks using dynamic global configuration"""
    max_workers = global_config.get("max_workers", 2)
    rate_limit = global_config.get("rate_limit", 50)
    
    print(f"Starting {max_workers} workers with rate limit {rate_limit}")
    
    # Workers can check for config changes
    while True:
        current_max = global_config.get("max_workers")
        if current_max != max_workers:
            print(f"Worker count changed from {max_workers} to {current_max}")
            max_workers = current_max
            # Restart workers with new count
        
        # Process with current configuration
        process_batch(rate_limit)

# File: admin/manager.py
"""Admin module that can update global config"""
from config.dynamic import global_config

def update_system_config(config_changes):
    """Update global configuration at runtime"""
    print("Updating global configuration...")
    global_config.update(config_changes)
    
    # Configuration changes immediately affect all modules
    print("Configuration update complete")

# Usage example
update_system_config({
    "max_workers": 8,
    "rate_limit": 200,
    "debug_mode": True
})
```

## **Repository-Wide Global Variables**

### **Environment Variable Management:**

```python
# File: config/environment.py
"""Environment variable management for the entire repository"""
import os
from typing import Optional, Dict, Any

class EnvironmentConfig:
    """Centralized environment variable management"""
    
    def __init__(self):
        self.config = self._load_environment_variables()
    
    def _load_environment_variables(self) -> Dict[str, Any]:
        """Load and validate environment variables"""
        config = {
            # Database configuration
            "DATABASE_URL": os.getenv("DATABASE_URL", "postgresql://localhost:5432/app"),
            "DATABASE_POOL_SIZE": int(os.getenv("DATABASE_POOL_SIZE", "10")),
            
            # Redis configuration  
            "REDIS_URL": os.getenv("REDIS_URL", "redis://localhost:6379"),
            "REDIS_TIMEOUT": int(os.getenv("REDIS_TIMEOUT", "5")),
            
            # API configuration
            "API_KEY": os.getenv("API_KEY"),  # Required
            "API_SECRET": os.getenv("API_SECRET"),  # Required
            "API_BASE_URL": os.getenv("API_BASE_URL", "https://api.example.com"),
            
            # Application configuration
            "ENVIRONMENT": os.getenv("ENVIRONMENT", "development"),
            "DEBUG": os.getenv("DEBUG", "false").lower() == "true",
            "LOG_LEVEL": os.getenv("LOG_LEVEL", "INFO"),
            
            # Security configuration
            "SECRET_KEY": os.getenv("SECRET_KEY"),  # Required
            "JWT_EXPIRY": int(os.getenv("JWT_EXPIRY", "3600")),
            
            # Performance configuration
            "MAX_WORKERS": int(os.getenv("MAX_WORKERS", "4")),
            "RATE_LIMIT": int(os.getenv("RATE_LIMIT", "100")),
            "TIMEOUT_SECONDS": int(os.getenv("TIMEOUT_SECONDS", "30")),
        }
        
        # Validate required variables
        required_vars = ["API_KEY", "API_SECRET", "SECRET_KEY"]
        missing_vars = [var for var in required_vars if not config[var]]
        
        if missing_vars:
            raise ValueError(f"Missing required environment variables: {missing_vars}")
        
        return config
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value"""
        return self.config.get(key, default)
    
    def is_production(self) -> bool:
        """Check if running in production environment"""
        return self.config["ENVIRONMENT"].lower() == "production"
    
    def is_development(self) -> bool:
        """Check if running in development environment"""
        return self.config["ENVIRONMENT"].lower() == "development"
    
    def get_database_config(self) -> Dict[str, Any]:
        """Get database-specific configuration"""
        return {
            "url": self.config["DATABASE_URL"],
            "pool_size": self.config["DATABASE_POOL_SIZE"],
            "timeout": self.config["TIMEOUT_SECONDS"]
        }
    
    def get_redis_config(self) -> Dict[str, Any]:
        """Get Redis-specific configuration"""
        return {
            "url": self.config["REDIS_URL"],
            "timeout": self.config["REDIS_TIMEOUT"]
        }

# Global instance available throughout the repository
env_config = EnvironmentConfig()

# File: utils/logger.py
"""Repository-wide logging configuration"""
from config.environment import env_config
import logging
import sys

def setup_repository_logging():
    """Setup logging for the entire repository"""
    log_level = env_config.get("LOG_LEVEL", "INFO")
    debug_mode = env_config.get("DEBUG", False)
    environment = env_config.get("ENVIRONMENT", "development")
    
    # Configure log format based on environment
    if environment == "production":
        log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    else:
        log_format = '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
    
    # Configure logging
    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format=log_format,
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(f'app_{environment}.log')
        ]
    )
    
    # Add debug information if in debug mode
    if debug_mode:
        logging.getLogger().setLevel(logging.DEBUG)
        logging.debug("Debug mode enabled")
        logging.debug(f"Configuration loaded: {env_config.config}")

# File: services/database.py
"""Database service using repository-wide configuration"""
from config.environment import env_config
import logging

logger = logging.getLogger(__name__)

class DatabaseService:
    """Database service using global environment configuration"""
    
    def __init__(self):
        self.config = env_config.get_database_config()
        self.connection = None
        logger.info(f"Database service initialized for {env_config.get('ENVIRONMENT')}")
    
    def connect(self):
        """Connect to database using global configuration"""
        try:
            database_url = self.config["url"]
            pool_size = self.config["pool_size"]
            timeout = self.config["timeout"]
            
            logger.info(f"Connecting to database: {database_url}")
            logger.info(f"Pool size: {pool_size}, Timeout: {timeout}s")
            
            # Create connection with global settings
            self.connection = create_db_connection(
                url=database_url,
                pool_size=pool_size,
                timeout=timeout
            )
            
            logger.info("Database connection established")
            return self.connection
            
        except Exception as e:
            logger.error(f"Database connection failed: {e}")
            raise

# File: services/cache.py
"""Cache service using repository-wide configuration"""
from config.environment import env_config
import redis
import logging

logger = logging.getLogger(__name__)

class CacheService:
    """Cache service using global environment configuration"""
    
    def __init__(self):
        self.config = env_config.get_redis_config()
        self.client = None
        logger.info("Cache service initialized")
    
    def connect(self):
        """Connect to Redis using global configuration"""
        try:
            redis_url = self.config["url"]
            timeout = self.config["timeout"]
            
            logger.info(f"Connecting to Redis: {redis_url}")
            
            self.client = redis.from_url(redis_url, socket_timeout=timeout)
            
            # Test connection
            self.client.ping()
            logger.info("Redis connection established")
            
            return self.client
            
        except Exception as e:
            logger.error(f"Redis connection failed: {e}")
            raise
```

### **Configuration File Management:**

```python
# File: config/file_config.py
"""File-based configuration management for repository-wide settings"""
import json
import yaml
import os
from pathlib import Path
from typing import Dict, Any, Optional

class FileConfigManager:
    """Manage configuration files for the entire repository"""
    
    def __init__(self, config_dir: str = "config"):
        self.config_dir = Path(config_dir)
        self.config_cache = {}
        self._load_all_configs()
    
    def _load_all_configs(self):
        """Load all configuration files in the config directory"""
        config_files = {
            "app": "app.yaml",
            "database": "database.yaml", 
            "api": "api.yaml",
            "logging": "logging.yaml",
            "security": "security.yaml"
        }
        
        for config_name, filename in config_files.items():
            config_path = self.config_dir / filename
            if config_path.exists():
                self.config_cache[config_name] = self._load_yaml_file(config_path)
            else:
                print(f"Warning: Configuration file {filename} not found")
                self.config_cache[config_name] = {}
    
    def _load_yaml_file(self, file_path: Path) -> Dict[str, Any]:
        """Load YAML configuration file"""
        try:
            with open(file_path, 'r') as file:
                return yaml.safe_load(file) or {}
        except Exception as e:
            print(f"Error loading {file_path}: {e}")
            return {}
    
    def get_config(self, config_name: str, environment: str = "production") -> Dict[str, Any]:
        """Get configuration for specific component and environment"""
        if config_name not in self.config_cache:
            return {}
        
        config = self.config_cache[config_name]
        
        # Get base configuration
        base_config = config.get("default", {})
        
        # Override with environment-specific configuration
        env_config = config.get(environment, {})
        
        # Merge configurations
        merged_config = {**base_config, **env_config}
        
        return merged_config
    
    def get_database_config(self, environment: str = "production") -> Dict[str, Any]:
        """Get database configuration for environment"""
        return self.get_config("database", environment)
    
    def get_api_config(self, environment: str = "production") -> Dict[str, Any]:
        """Get API configuration for environment"""
        return self.get_config("api", environment)
    
    def reload_configs(self):
        """Reload all configuration files"""
        print("Reloading configuration files...")
        self.config_cache.clear()
        self._load_all_configs()
        print("Configuration reload complete")

# Example configuration files:

# config/app.yaml
"""
default:
  name: "DevOps Application"
  version: "1.0.0"
  max_workers: 4
  timeout: 30
  
development:
  debug: true
  max_workers: 2
  timeout: 60
  
production:
  debug: false
  max_workers: 8
  timeout: 15
  
staging:
  debug: false
  max_workers: 4
  timeout: 30
"""

# config/database.yaml
"""
default:
  pool_size: 10
  timeout: 30
  retry_attempts: 3
  
development:
  host: "localhost"
  port: 5432
  database: "app_dev"
  pool_size: 5
  
production:
  host: "prod-db.example.com"
  port: 5432
  database: "app_prod"
  pool_size: 20
  ssl_required: true
  
staging:
  host: "staging-db.example.com"
  port: 5432
  database: "app_staging"
  pool_size: 10
"""

# Global instance for repository-wide use
file_config = FileConfigManager()

# File: main.py
"""Main application using repository-wide configuration"""
from config.file_config import file_config
from config.environment import env_config
from utils.logger import setup_repository_logging
from services.database import DatabaseService
from services.cache import CacheService

def initialize_application():
    """Initialize application with repository-wide configuration"""
    # Get current environment
    environment = env_config.get("ENVIRONMENT", "production")
    
    print(f"Initializing application for {environment} environment")
    
    # Setup repository-wide logging
    setup_repository_logging()
    
    # Get application configuration
    app_config = file_config.get_config("app", environment)
    database_config = file_config.get_config("database", environment)
    
    print(f"Application: {app_config.get('name')} v{app_config.get('version')}")
    print(f"Max workers: {app_config.get('max_workers')}")
    print(f"Database host: {database_config.get('host')}")
    
    # Initialize services with global configuration
    db_service = DatabaseService()
    cache_service = CacheService()
    
    # Connect services
    db_service.connect()
    cache_service.connect()
    
    return {
        "database": db_service,
        "cache": cache_service,
        "config": {
            "app": app_config,
            "database": database_config
        }
    }

if __name__ == "__main__":
    app = initialize_application()
    print("Application initialized successfully")
```

### **Best Practices for Repository-Wide Variables:**

```python
# File: config/best_practices.py
"""Best practices for repository-wide variable management"""

# 1. Environment Variable Validation
def validate_environment():
    """Validate all required environment variables are set"""
    required_vars = [
        "DATABASE_URL",
        "API_KEY", 
        "SECRET_KEY",
        "ENVIRONMENT"
    ]
    
    missing_vars = []
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        raise EnvironmentError(f"Missing required environment variables: {missing_vars}")

# 2. Configuration Hierarchy (Environment > File > Defaults)
def get_hierarchical_config(key: str, default: Any = None) -> Any:
    """Get configuration with environment > file > default hierarchy"""
    
    # 1. Check environment variable first
    env_value = os.getenv(key.upper())
    if env_value is not None:
        return env_value
    
    # 2. Check configuration file
    file_value = file_config.get_config("app").get(key.lower())
    if file_value is not None:
        return file_value
    
    # 3. Return default
    return default

# 3. Secret Management
def load_secrets_safely():
    """Load secrets with fallback and validation"""
    secrets = {}
    
    # Try to load from secure secret store first
    try:
        secrets = load_from_secret_store()
    except Exception as e:
        print(f"Secret store unavailable: {e}")
        
        # Fallback to environment variables
        secrets = {
            "database_password": os.getenv("DATABASE_PASSWORD"),
            "api_secret": os.getenv("API_SECRET"),
            "encryption_key": os.getenv("ENCRYPTION_KEY")
        }
    
    # Validate all secrets are present
    missing_secrets = [k for k, v in secrets.items() if not v]
    if missing_secrets:
        raise ValueError(f"Missing secrets: {missing_secrets}")
    
    return secrets

# 4. Configuration Change Monitoring
class ConfigMonitor:
    """Monitor configuration changes and notify components"""
    
    def __init__(self):
        self.observers = []
        self.current_config = {}
    
    def register_observer(self, callback):
        """Register callback for configuration changes"""
        self.observers.append(callback)
    
    def check_for_changes(self):
        """Check for configuration changes and notify observers"""
        new_config = {
            "environment": os.getenv("ENVIRONMENT"),
            "debug": os.getenv("DEBUG", "false").lower() == "true",
            "max_workers": int(os.getenv("MAX_WORKERS", "4"))
        }
        
        if new_config != self.current_config:
            changes = {}
            for key, new_value in new_config.items():
                old_value = self.current_config.get(key)
                if old_value != new_value:
                    changes[key] = {"old": old_value, "new": new_value}
            
            if changes:
                print(f"Configuration changes detected: {changes}")
                for observer in self.observers:
                    observer(changes)
            
            self.current_config = new_config

# Global configuration monitor
config_monitor = ConfigMonitor()
```

## **Security Considerations for Global Variables**

### **Secure Secret Management:**

```python
# File: config/security.py
"""Secure handling of sensitive global variables"""
import os
import base64
from cryptography.fernet import Fernet
from typing import Dict, Optional

class SecureConfigManager:
    """Securely manage sensitive configuration variables"""
    
    def __init__(self):
        self.encryption_key = self._get_encryption_key()
        self.cipher_suite = Fernet(self.encryption_key) if self.encryption_key else None
        self.secure_vars = {}
    
    def _get_encryption_key(self) -> Optional[bytes]:
        """Get encryption key from environment"""
        key_b64 = os.getenv("CONFIG_ENCRYPTION_KEY")
        if key_b64:
            try:
                return base64.urlsafe_b64decode(key_b64)
            except Exception as e:
                print(f"Invalid encryption key format: {e}")
        return None
    
    def store_secure_variable(self, name: str, value: str):
        """Store encrypted sensitive variable"""
        if self.cipher_suite:
            encrypted_value = self.cipher_suite.encrypt(value.encode())
            self.secure_vars[name] = encrypted_value
        else:
            # Fallback: store as environment variable (less secure)
            os.environ[f"SECURE_{name}"] = value
    
    def get_secure_variable(self, name: str) -> Optional[str]:
        """Retrieve and decrypt sensitive variable"""
        if name in self.secure_vars and self.cipher_suite:
            try:
                decrypted_value = self.cipher_suite.decrypt(self.secure_vars[name])
                return decrypted_value.decode()
            except Exception as e:
                print(f"Failed to decrypt {name}: {e}")
                return None
        else:
            # Fallback: check environment variable
            return os.getenv(f"SECURE_{name}")
    
    def rotate_encryption_key(self, new_key: bytes):
        """Rotate encryption key and re-encrypt all variables"""
        if not self.cipher_suite:
            print("No current encryption key available")
            return
        
        # Decrypt all variables with old key
        decrypted_vars = {}
        for name, encrypted_value in self.secure_vars.items():
            try:
                decrypted_vars[name] = self.cipher_suite.decrypt(encrypted_value).decode()
            except Exception as e:
                print(f"Failed to decrypt {name} during rotation: {e}")
        
        # Update encryption key and cipher
        self.encryption_key = new_key
        self.cipher_suite = Fernet(new_key)
        
        # Re-encrypt all variables with new key
        for name, value in decrypted_vars.items():
            self.store_secure_variable(name, value)
        
        print(f"Encryption key rotated, {len(decrypted_vars)} variables re-encrypted")

# Global secure config manager
secure_config = SecureConfigManager()

# File: config/audit.py
"""Configuration access auditing"""
import logging
import time
from functools import wraps

# Setup audit logger
audit_logger = logging.getLogger("config_audit")
audit_logger.setLevel(logging.INFO)
handler = logging.FileHandler("config_audit.log")
handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
audit_logger.addHandler(handler)

def audit_config_access(func):
    """Decorator to audit configuration variable access"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        
        # Log access attempt
        config_name = args[0] if args else "unknown"
        audit_logger.info(f"CONFIG_ACCESS: {func.__name__} - {config_name}")
        
        try:
            result = func(*args, **kwargs)
            
            # Log successful access
            duration = time.time() - start_time
            audit_logger.info(f"CONFIG_SUCCESS: {config_name} - {duration:.3f}s")
            
            return result
            
        except Exception as e:
            # Log failed access
            audit_logger.error(f"CONFIG_ERROR: {config_name} - {str(e)}")
            raise
    
    return wrapper

# Apply auditing to configuration access
@audit_config_access
def get_audited_config(key: str, default=None):
    """Get configuration value with auditing"""
    return env_config.get(key, default)
```

**Connection to Instructor's Concept**: This builds on the instructor's scope foundation by showing practical DevOps scenarios where scope and lifetime directly impact script reliability and maintainability. 