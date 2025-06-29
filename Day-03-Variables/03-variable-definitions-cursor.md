# Advanced Variable Definitions - 4 Ways to Create Variables

---
## **⚡ WHEN CONFUSED - READ THIS FIRST! ⚡**
**Simple = Just type it | Complex = Lists/tuples | External = From files/databases | Import = From other files**

```python
# SIMPLE - Single values you type
DATABASE_URL = "postgresql://prod-db:5432/app"

# COMPLEX - Multiple values you create
servers = ["web-01", "web-02", "db-01"]

# EXTERNAL - Data from outside sources  
users = cursor.fetchall()  # From database

# IMPORT - Variables from other files
from config import DATABASE_URL
```
---

## **The 4 Ways to Define Variables**

### **1. Simple Variables - Direct Assignment**

**What it is:** You directly assign a single value to a variable name.

```python
# DevOps Configuration Examples
DATABASE_URL = "postgresql://prod-db:5432/myapp"
API_KEY = "sk-1234567890abcdef"
ENVIRONMENT = "production"
MAX_RETRIES = 3
TIMEOUT_SECONDS = 30
DEBUG_MODE = False
APPLICATION_NAME = "WebAPI"
VERSION = "1.2.3"

# Server Configuration
DEFAULT_PORT = 8080
SSL_ENABLED = True
LOG_LEVEL = "INFO"
BACKUP_RETENTION_DAYS = 30
```

**When to use:** Configuration values, constants, settings that rarely change.

**Benefits:**
- Simple and clear
- Easy to modify
- Good for single values
- Perfect for configuration

### **2. Complex Variables - Data Structures**

**What it is:** Variables that contain multiple values using lists, tuples, dictionaries.

#### **Lists - Multiple Similar Items**
```python
# Server Lists
WEB_SERVERS = ["web-01", "web-02", "web-03"]  # Variable 'WEB_SERVERS' contains 3 server names
DATABASE_SERVERS = ["db-primary", "db-replica-01", "db-replica-02"]  # Variable 'DATABASE_SERVERS' contains 3 DB names
ENVIRONMENTS = ["development", "staging", "production"]  # Variable 'ENVIRONMENTS' contains 3 environment names
SUPPORTED_REGIONS = ["us-east-1", "us-west-2", "eu-west-1"]  # Variable 'SUPPORTED_REGIONS' contains 3 region names

# File Extensions to Monitor
LOG_FILE_EXTENSIONS = [".log", ".txt", ".json"]  # Variable 'LOG_FILE_EXTENSIONS' contains 3 file extensions
BACKUP_FILE_TYPES = [".sql", ".tar.gz", ".zip"]  # Variable 'BACKUP_FILE_TYPES' contains 3 backup types

# HOW DO WE KNOW WHAT EACH LIST ITEM REPRESENTS?
# FOR LISTS - All items must be the same TYPE of data:
WEB_SERVERS = ["web-01", "web-02", "web-03"]              # ALL are server names (strings)
SERVER_PORTS = [80, 443, 8080, 9000]                      # ALL are port numbers (integers)  
SERVER_IPS = ["192.168.1.10", "192.168.1.11"]            # ALL are IP addresses (strings)
IS_PRODUCTION = [True, False, True, False]                # ALL are boolean values

# The variable name should tell you what type of data is inside:
# WEB_SERVERS = contains server names
# SERVER_PORTS = contains port numbers
# SERVER_IPS = contains IP addresses

# Usage with lists - WHERE LOOP VARIABLE GETS ITS VALUES:
for server in WEB_SERVERS:  # 'server' gets each name from WEB_SERVERS list
    deploy_to_server(server)  # server = "web-01", then "web-02", then "web-03"
    
# EXPLANATION:
# WEB_SERVERS = the list variable name (you define this)
# ["web-01", "web-02", "web-03"] = the actual server names inside the list
# server = the loop variable name (you choose this, could be 'web_server', 's', anything)
# server gets each value from the list: first "web-01", then "web-02", then "web-03"
```

#### **Tuples - Fixed Related Data**

**🔥 CRITICAL: Position in tuples MATTERS - YOU decide what each position means!**

```python
# Server Information (name, ip, type) - YOU decide this order!
MAIN_SERVERS = [  # Variable 'MAIN_SERVERS' contains a list of server tuples
    ("web-01", "192.168.1.10", "web"),      # Position 0=name, Position 1=ip, Position 2=type
    ("web-02", "192.168.1.11", "web"),      # Position 0=name, Position 1=ip, Position 2=type
    ("db-01", "192.168.1.20", "database"),  # Position 0=name, Position 1=ip, Position 2=type
    ("cache-01", "192.168.1.30", "redis")   # Position 0=name, Position 1=ip, Position 2=type
]

# Database Connection Info (host, port, database) - Different order than above!
DATABASE_CONFIGS = [  # Variable 'DATABASE_CONFIGS' contains a list of database tuples
    ("prod-db", 5432, "app_production"),    # Position 0=host, Position 1=port, Position 2=database
    ("staging-db", 5432, "app_staging"),    # Position 0=host, Position 1=port, Position 2=database 
    ("dev-db", 5432, "app_development")     # Position 0=host, Position 1=port, Position 2=database
]

# HOW DO WE KNOW WHAT EACH POSITION MEANS?
# 1. YOU decide the order when creating the tuples
# 2. You document it in comments like: (name, ip, type)
# 3. You must remember the order when unpacking

# SAME DATA, DIFFERENT ORDERS (both valid, but different!):
# Option 1: (name, ip, type)
servers_option1 = [("web-01", "192.168.1.10", "web")]

# Option 2: (ip, name, type) - different order!
servers_option2 = [("192.168.1.10", "web-01", "web")]

# Option 3: (type, name, ip) - yet another order!
servers_option3 = [("web", "web-01", "192.168.1.10")]

# Usage with tuples - HOW UNPACKING WORKS:
for server_name, ip_address, server_type in MAIN_SERVERS:  # Must match the order you defined!
    configure_server(server_name, ip_address, server_type)  # Each variable becomes a parameter!

# 🔥 CRITICAL: HOW FUNCTIONS KNOW WHAT EACH PARAMETER MEANS

def configure_server(name, ip, type):  # Function defines: position 0=name, position 1=ip, position 2=type
    print(f"Configuring server {name} at {ip} as {type}")

# Your tuple structure: ("web-01", "192.168.1.10", "web")
#                       Position 0   Position 1      Position 2

# When you call: configure_server(server_name, ip_address, server_type)
# Python passes: configure_server("web-01", "192.168.1.10", "web")
#                                 Position 0  Position 1      Position 2

# THE FUNCTION DOESN'T KNOW ABOUT YOUR TUPLE STRUCTURE OR WHICH VARIABLE YOU'RE USING!
# It just receives individual values: name="web-01", ip="192.168.1.10", type="web"
# The function has NO IDEA these came from MAIN_SERVERS vs any other variable!
# Order MUST match: tuple position → function parameter position

# 🔥 CRITICAL: THE FUNCTION DOESN'T KNOW WHICH VARIABLE YOU USE!

# Let's say you have multiple server variables:
MAIN_SERVERS = [("web-01", "192.168.1.10", "web")]        # name, ip, type
BACKUP_SERVERS = [("backup-01", "192.168.2.10", "backup")] # name, ip, type  
TEST_SERVERS = [("test-01", "192.168.3.10", "test")]      # name, ip, type
DATABASE_CONFIGS = [("prod-db", 5432, "postgresql")]       # host, port, type - DIFFERENT structure!

def configure_server(name, ip, type):
    print(f"Configuring {name} at {ip} as {type}")

# YOU choose which variable to use:

# Option 1: Use MAIN_SERVERS
for server_name, ip_address, server_type in MAIN_SERVERS:  # YOU chose MAIN_SERVERS here!
    configure_server(server_name, ip_address, server_type)

# Option 2: Use BACKUP_SERVERS  
for server_name, ip_address, server_type in BACKUP_SERVERS:  # YOU chose BACKUP_SERVERS here!
    configure_server(server_name, ip_address, server_type)

# Option 3: Use TEST_SERVERS
for server_name, ip_address, server_type in TEST_SERVERS:  # YOU chose TEST_SERVERS here!
    configure_server(server_name, ip_address, server_type)

# WRONG: Using DATABASE_CONFIGS (different structure!)
# for server_name, ip_address, server_type in DATABASE_CONFIGS:  # WRONG! Different tuple structure
#     configure_server(server_name, ip_address, server_type)  # Would pass: ("prod-db", 5432, "postgresql")
#     # Function would get: name="prod-db", ip=5432, type="postgresql" - ip is a number, not IP address!

# THE FUNCTION ONLY KNOWS WHAT YOU EXPLICITLY PASS TO IT!

# WHAT HAPPENS IF ORDER DOESN'T MATCH:
# If your tuple was: ("192.168.1.10", "web-01", "web") - ip, name, type
# But function expects: (name, ip, type)
# Result: configure_server("192.168.1.10", "web-01", "web")
#         Function thinks: name="192.168.1.10", ip="web-01", type="web" - WRONG!

# YOU MUST MATCH TUPLE ORDER TO FUNCTION PARAMETER ORDER:

# Option 1: Design tuple to match function
server_data = ("web-01", "192.168.1.10", "web")  # (name, ip, type)
def configure_server(name, ip, type):  # Same order as tuple
    pass

# Option 2: Design function to match tuple  
server_data = ("192.168.1.10", "web-01", "web")  # (ip, name, type)
def configure_server(ip, name, type):  # Same order as tuple
    pass

# Option 3: Unpack in specific order to match function
server_data = ("192.168.1.10", "web-01", "web")  # (ip, name, type)
ip, name, type = server_data  # Unpack to separate variables
configure_server(name, ip, type)  # Reorder to match function: (name, ip, type)

# If you used servers_option2 above, you'd need to unpack differently:
# for ip_address, server_name, server_type in servers_option2:  # Different order!
#     configure_server(server_name, ip_address, server_type)  # Reorder when calling function!
    
# DETAILED EXPLANATION:
# MAIN_SERVERS = the list variable name (you define this, you CHOOSE to use this specific variable)
# [("web-01", "192.168.1.10", "web"), ...] = list containing tuples
# ("web-01", "192.168.1.10", "web") = first tuple with 3 pieces of data in YOUR chosen order
# server_name, ip_address, server_type = 3 loop variables (you choose these names)
# 
# The unpacking MUST match your tuple order:
# server_name gets position 0 = "web-01"
# ip_address gets position 1 = "192.168.1.10"  
# server_type gets position 2 = "web"
# 
# First iteration: server_name="web-01", ip_address="192.168.1.10", server_type="web"  
# Second iteration: server_name="web-02", ip_address="192.168.1.11", server_type="web"
# Third iteration: server_name="db-01", ip_address="192.168.1.20", server_type="database"
#
# 🔥 KEY POINT: The function configure_server() has NO IDEA which variable you used! 🔥
# It just receives the VALUES: configure_server("web-01", "192.168.1.10", "web")
# You could have used MAIN_SERVERS, BACKUP_SERVERS, TEST_SERVERS, or any other compatible variable
# The function only cares about getting 3 string values in the right order

# === CRITICAL UNDERSTANDING: Function Variable Confusion Solved ===

# Let's say you have multiple variables with the SAME 3-item structure:
USERS_DATA = [("john", "admin", "john@company.com"), ("sarah", "user", "sarah@company.com")]
FUNCTIONS_DATA = [("backup", "daily", "backup@system.com"), ("monitor", "hourly", "monitor@system.com")]
SERVERS_DATA = [("web-01", "active", "web-01@system.com"), ("db-01", "standby", "db-01@system.com")]

def create_user_account(username, user_role, email_address):
    print(f"Creating account for {username} ({user_role}) - Email: {email_address}")

# HERE'S THE INSIGHT: YOU decide which variable to use, function doesn't know!

print("=== Choice 1: Using USERS_DATA (makes sense) ===")
for user in USERS_DATA:
    create_user_account(user[0], user[1], user[2])
    # Function receives: ("john", "admin", "john@company.com")
    # Function has NO IDEA this came from USERS_DATA variable
    # Result: "Creating account for john (admin) - Email: john@company.com"

print("\n=== Choice 2: Using FUNCTIONS_DATA (technically works but wrong!) ===")
for func in FUNCTIONS_DATA:
    create_user_account(func[0], func[1], func[2])
    # Function receives: ("backup", "daily", "backup@system.com")
    # Function has NO IDEA this came from FUNCTIONS_DATA variable
    # Result: "Creating account for backup (daily) - Email: backup@system.com"
    # This works but makes no business sense!

print("\n=== Choice 3: Using SERVERS_DATA (also works but wrong!) ===")
for server in SERVERS_DATA:
    create_user_account(server[0], server[1], server[2])
    # Function receives: ("web-01", "active", "web-01@system.com")
    # Function has NO IDEA this came from SERVERS_DATA variable
    # Result: "Creating account for web-01 (active) - Email: web-01@system.com"
    # This also works but makes no business sense!

# 🔥 THE FUNCTION ONLY SEES THE VALUES, NOT THE VARIABLE NAMES! 🔥
# create_user_account("john", "admin", "john@company.com") ← This is all the function gets
# It doesn't know if you used:
# - USERS_DATA[0]  
# - FUNCTIONS_DATA[0]
# - SERVERS_DATA[0]
# - Or any other variable with 3 string items!

# THE POWER AND RESPONSIBILITY IS YOURS:
# ✅ You can use the same function with different data sources
# ✅ Function is reusable and flexible
# ⚠️  You must choose the RIGHT variable that makes sense for your task
# ⚠️  You must ensure tuple structure matches function parameters

# PRACTICAL DEVOPS EXAMPLE:
dev_users = [("alice", "developer", "alice@dev.com")]
admin_users = [("bob", "admin", "bob@admin.com")]
test_users = [("charlie", "tester", "charlie@test.com")]

# You can use the SAME function for different user types:
for user in dev_users:
    create_user_account(user[0], user[1], user[2])  # Dev users

for user in admin_users:  
    create_user_account(user[0], user[1], user[2])  # Admin users

for user in test_users:
    create_user_account(user[0], user[1], user[2])  # Test users

# Function doesn't know which user type it's processing!
# It just processes whatever data YOU give it!

# ⚡⚡⚡ BREAKTHROUGH UNDERSTANDING: UNPACKING IS WHERE YOU DECIDE! ⚡⚡⚡
# 
# UNPACKING = Where YOU choose which variable and its tuples the function gets!
#
# for user in USERS_DATA:               ← YOU chose 'USERS_DATA' variable here!
#     create_user_account(user[0], user[1], user[2])  ← Unpacking USERS_DATA tuples
#
# for func in FUNCTIONS_DATA:           ← YOU chose 'FUNCTIONS_DATA' variable here!  
#     create_user_account(func[0], func[1], func[2])  ← Unpacking FUNCTIONS_DATA tuples
#
# for server in SERVERS_DATA:           ← YOU chose 'SERVERS_DATA' variable here!
#     create_user_account(server[0], server[1], server[2])  ← Unpacking SERVERS_DATA tuples
#
# The function doesn't know which variable you picked - YOU control it with unpacking!
# This is the POWER of understanding unpacking - you decide what data the function processes!
```

#### **Dictionaries - Key-Value Configuration**
```python
# Environment-Specific Settings
ENVIRONMENT_CONFIG = {
    "development": {
        "database_url": "postgresql://localhost:5432/app_dev",
        "debug": True,
        "replicas": 1,
        "log_level": "DEBUG"
    },
    "production": {
        "database_url": "postgresql://prod-db:5432/app_prod", 
        "debug": False,
        "replicas": 3,
        "log_level": "ERROR"
    }
}

# Server Resource Limits
RESOURCE_LIMITS = {
    "web": {"cpu": "500m", "memory": "1Gi", "storage": "10Gi"},
    "database": {"cpu": "2000m", "memory": "4Gi", "storage": "100Gi"},
    "cache": {"cpu": "250m", "memory": "512Mi", "storage": "5Gi"}
}

# Usage with dictionaries
def deploy_to_environment(app_name, environment):
    config = ENVIRONMENT_CONFIG[environment]  # Get config for specific environment
    deploy_app(app_name, config["database_url"], config["replicas"])  # Use config as parameters!
```

**When to use:** When you have multiple related items, server lists, configuration options.

### **3. External Variables - From Outside Sources**

**What it is:** Variables whose values come from files, databases, APIs, or other external sources.

#### **From Files**
```python
# JSON Configuration Files
import json

# Load server inventory from file
with open("config/servers.json", "r") as f:  # Open the file named "servers.json"
    SERVERS_FROM_FILE = json.load(f)  # Variable 'SERVERS_FROM_FILE' gets data from JSON file
# Result: [{"name": "web-01", "ip": "192.168.1.10", "type": "web"}, ...]
# Each dictionary contains: {"name": server_name_from_file, "ip": ip_from_file, "type": type_from_file}

# EXPLANATION:
# "config/servers.json" = the filename (you specify this path)
# SERVERS_FROM_FILE = variable name for the loaded data (you choose this)
# json.load(f) = reads and converts JSON file to Python data structure
# [{"name": "web-01", ...}, ...] = actual data structure from the file

# Load environment variables from .env file
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL_FROM_ENV = os.getenv("DATABASE_URL")
API_KEY_FROM_ENV = os.getenv("API_KEY")

# CSV Files (user lists, server inventories)
import csv

with open("users.csv", "r") as f:
    reader = csv.reader(f)
    USERS_FROM_CSV = list(reader)
# Result: [["alice", "admin", "alice@co.com"], ["bob", "user", "bob@co.com"]]

# YAML Configuration (Kubernetes, Docker Compose)
import yaml

with open("config/deployment.yaml", "r") as f:
    DEPLOYMENT_CONFIG = yaml.safe_load(f)
```

#### **From Databases**
```python
# PostgreSQL Database
import psycopg2

connection = psycopg2.connect(DATABASE_URL)
cursor = connection.cursor()

# Get all active users
cursor.execute("SELECT username, email, role FROM users WHERE active = true")
ACTIVE_USERS = cursor.fetchall()  # Variable 'ACTIVE_USERS' gets data from database
# Result: [("alice", "alice@co.com", "admin"), ("bob", "bob@co.com", "user")]
# Each tuple contains: (username_from_db, email_from_db, role_from_db)

# Get server monitoring data
cursor.execute("""
    SELECT server_name, cpu_usage, memory_usage, last_checked 
    FROM server_metrics 
    WHERE last_checked > NOW() - INTERVAL '1 hour'
""")
RECENT_METRICS = cursor.fetchall()  # Variable 'RECENT_METRICS' gets server data from database

# Usage with database results - HOW DATABASE COLUMNS BECOME VARIABLES:
for username, email, role in ACTIVE_USERS:  # Unpack each database row into 3 variables
    setup_user_account(username, email, role)  # Database columns become function parameters!
    
# DETAILED EXPLANATION:
# cursor.execute("SELECT username, email, role FROM users...") = SQL query selects 3 columns
# ACTIVE_USERS = variable name for the results (you choose this)
# cursor.fetchall() = returns list of tuples from database
# [("alice", "alice@co.com", "admin"), ...] = actual data returned by database
# ("alice", "alice@co.com", "admin") = first row from database as a tuple
# username, email, role = loop variables (you choose these names, often match column names)
#
# First iteration: username="alice", email="alice@co.com", role="admin" (first database row)
# Second iteration: username="bob", email="bob@co.com", role="user" (second database row)
```

#### **From APIs**
```python
# REST API Calls
import requests

# Get server status from monitoring API
response = requests.get("https://monitoring.company.com/api/servers")
SERVERS_FROM_API = response.json()
# Result: [{"name": "web-01", "status": "healthy", "uptime": "99.9%"}, ...]

# Get deployment information
deploy_response = requests.get("https://deploy.company.com/api/deployments/latest")
LATEST_DEPLOYMENTS = deploy_response.json()

# Docker API (list containers)
docker_response = requests.get("http://localhost:2376/containers/json")
RUNNING_CONTAINERS = docker_response.json()

# Kubernetes API (get pods)
k8s_response = requests.get(
    "https://k8s-api.company.com/api/v1/namespaces/default/pods",
    headers={"Authorization": f"Bearer {K8S_TOKEN}"}
)
KUBERNETES_PODS = k8s_response.json()["items"]

# Usage with API data
for server in SERVERS_FROM_API:
    if server["status"] != "healthy":
        alert_on_server(server["name"], server["status"])  # API data as parameters!
```

#### **From Command Line Tools**
```python
# Shell Commands
import subprocess

# Get system information
result = subprocess.run(["df", "-h"], capture_output=True, text=True)
DISK_USAGE = result.stdout.split('\n')

# Get Docker containers
docker_result = subprocess.run(["docker", "ps", "--format", "table"], capture_output=True, text=True)
DOCKER_CONTAINERS = docker_result.stdout.split('\n')

# Get Git information  
git_result = subprocess.run(["git", "log", "--oneline", "-5"], capture_output=True, text=True)
RECENT_COMMITS = git_result.stdout.split('\n')
```

**When to use:** When data changes frequently, comes from external systems, or is too large to hardcode.

### **4. Import Variables - From Other Files**

**What it is:** Variables defined in other Python files that you import into your current file.

#### **Basic Imports**
```python
# File: config/database.py
DATABASE_URL = "postgresql://prod-db:5432/app"
DATABASE_USER = "app_user"
DATABASE_PASSWORD = "secret123"
CONNECTION_POOL_SIZE = 10

# File: config/api.py  
API_BASE_URL = "https://api.company.com"
API_KEY = "sk-1234567890abcdef"
API_TIMEOUT = 30

# File: main.py - Import and use
from config.database import DATABASE_URL, DATABASE_USER, CONNECTION_POOL_SIZE  # Import 3 variables from database.py
from config.api import API_BASE_URL, API_KEY  # Import 2 variables from api.py

# EXPLANATION:
# config.database = the file path (config/database.py)
# DATABASE_URL, DATABASE_USER, CONNECTION_POOL_SIZE = variable names from that file (defined there)
# Now you can use these variables as if you defined them in this file

def connect_to_database():
    return create_connection(DATABASE_URL, DATABASE_USER, pool_size=CONNECTION_POOL_SIZE)
    # DATABASE_URL comes from config/database.py
    # DATABASE_USER comes from config/database.py  
    # CONNECTION_POOL_SIZE comes from config/database.py

def call_api(endpoint):
    return requests.get(f"{API_BASE_URL}{endpoint}", headers={"Authorization": API_KEY})
    # API_BASE_URL comes from config/api.py
    # API_KEY comes from config/api.py
    # endpoint comes from the function parameter (passed when called)
```

#### **Complex Data Imports**
```python
# File: config/servers.py
PRODUCTION_SERVERS = [
    {"name": "web-01", "ip": "192.168.1.10", "type": "web", "region": "us-east-1"},
    {"name": "web-02", "ip": "192.168.1.11", "type": "web", "region": "us-east-1"},
    {"name": "db-01", "ip": "192.168.1.20", "type": "database", "region": "us-east-1"}
]

STAGING_SERVERS = [
    {"name": "staging-web", "ip": "10.0.1.10", "type": "web", "region": "us-west-2"},
    {"name": "staging-db", "ip": "10.0.1.20", "type": "database", "region": "us-west-2"}
]

ENVIRONMENT_CONFIGS = {
    "production": {
        "servers": PRODUCTION_SERVERS,
        "replicas": 3,
        "backup_enabled": True,
        "monitoring_interval": 60
    },
    "staging": {
        "servers": STAGING_SERVERS, 
        "replicas": 1,
        "backup_enabled": False,
        "monitoring_interval": 300
    }
}

# File: deployment.py - Import and use
from config.servers import PRODUCTION_SERVERS, ENVIRONMENT_CONFIGS

def deploy_to_production(app_name):
    config = ENVIRONMENT_CONFIGS["production"]
    servers = config["servers"]
    
    for server in servers:  # Imported data becomes loop parameters!
        deploy_app_to_server(app_name, server["name"], server["ip"], server["type"])
```

#### **Dynamic Imports**
```python
# File: environments/production.py
DATABASE_URL = "postgresql://prod-db:5432/app"
REDIS_URL = "redis://prod-cache:6379/0"
REPLICAS = 3

# File: environments/staging.py  
DATABASE_URL = "postgresql://staging-db:5432/app"
REDIS_URL = "redis://staging-cache:6379/0"
REPLICAS = 1

# File: app.py - Dynamic environment loading
import os
import importlib

# Load configuration based on environment
ENVIRONMENT = os.getenv("ENVIRONMENT", "staging")
config_module = importlib.import_module(f"environments.{ENVIRONMENT}")

DATABASE_URL = config_module.DATABASE_URL
REDIS_URL = config_module.REDIS_URL  
REPLICAS = config_module.REPLICAS

print(f"Running in {ENVIRONMENT} with {REPLICAS} replicas")
```

**When to use:** Shared configuration, reusable constants, environment-specific settings.

## **Combining All 4 Types - Real DevOps Example**

```python
# File: main.py - Using all 4 variable definition types

# 1. SIMPLE VARIABLES - Direct configuration
COMPANY_NAME = "TechCorp"
APPLICATION_VERSION = "2.1.0"
DEFAULT_TIMEOUT = 30

# 2. COMPLEX VARIABLES - Structured data we create
ALERT_RECIPIENTS = ["devops@company.com", "oncall@company.com"]
BACKUP_SCHEDULE = [
    ("daily", "02:00", 7),    # type, time, retention_days
    ("weekly", "03:00", 30),
    ("monthly", "04:00", 365)
]

# 3. EXTERNAL VARIABLES - From outside sources
import json
import psycopg2
from config.database import DATABASE_URL

# From file
with open("config/servers.json") as f:
    SERVERS_INVENTORY = json.load(f)

# From database
connection = psycopg2.connect(DATABASE_URL)
cursor = connection.cursor()
cursor.execute("SELECT username, email, role FROM users WHERE active = true")
ACTIVE_USERS = cursor.fetchall()

# 4. IMPORT VARIABLES - From other files
from config.monitoring import ALERT_THRESHOLD, MONITORING_INTERVAL
from config.deployment import PRODUCTION_CONFIG, STAGING_CONFIG

# Usage - All types working together
def run_daily_operations():
    print(f"Starting {COMPANY_NAME} operations v{APPLICATION_VERSION}")
    
    # Use simple variables
    timeout = DEFAULT_TIMEOUT
    
    # Use complex variables (loop with parameters!)
    for schedule_type, time, retention in BACKUP_SCHEDULE:
        schedule_backup(schedule_type, time, retention)
    
    # Use external variables (database results as parameters!)
    for username, email, role in ACTIVE_USERS:
        send_daily_report(username, email, role)
    
    # Use imported variables
    if check_system_health() > ALERT_THRESHOLD:
        for recipient in ALERT_RECIPIENTS:
            send_alert(recipient, "System health critical")

# The power of combining all 4 types:
# - Simple: Configuration that rarely changes
# - Complex: Multiple related items you define
# - External: Dynamic data from outside sources  
# - Import: Shared configuration across files
```

## **Decision Guide - Which Type to Use When**

### **📋 Quick Decision Tree:**

**1. Is it a single value that rarely changes?**
- Yes → **Simple variable** (`DATABASE_URL = "..."`)

**2. Is it multiple related items you're defining yourself?**
- Yes → **Complex variable** (`servers = ["web-01", "web-02"]`)

**3. Does the data come from files, databases, or APIs?**
- Yes → **External variable** (`users = cursor.fetchall()`)

**4. Do you need to share it across multiple files?**
- Yes → **Import variable** (`from config import DATABASE_URL`)

### **🔧 DevOps Patterns:**

**✅ Simple Variables:**
- Database connection strings
- API keys and secrets
- Default timeouts and limits
- Application metadata

**✅ Complex Variables:**
- Server inventories you maintain
- Configuration options and choices
- File patterns and extensions
- Multi-step processes

**✅ External Variables:**
- User lists from databases
- Server metrics from monitoring APIs
- Configuration from files
- Dynamic inventory from cloud providers

**✅ Import Variables:**
- Environment-specific configuration
- Shared constants across modules
- Reusable server lists
- Common utility settings

### **💡 The Golden Rule:**
**Choose the simplest type that meets your needs, then upgrade when you need more flexibility!**

Start with simple variables, move to complex when you have multiple items, use external when data changes frequently, and use imports when sharing across files.

Understanding these 4 types gives you the foundation for any DevOps automation task! 🚀

## **Real-World Beginner Developer Workflow**

### **Example 1: Learning Progression - Server Management**

```python
# === BEGINNER DEVOPS DEVELOPER LEARNING JOURNEY ===

print("=== Step 1: Starting Simple (Day 1) ===")
# Beginner starts with individual variables (hardest to scale)
server_name = "web-01"
server_ip = "192.168.1.10"
server_port = 80

def deploy_to_server(name, ip, port):
    print(f"Deploying to {name} at {ip}:{port}")

# Works for one server
deploy_to_server(server_name, server_ip, server_port)

print("\n=== Step 2: Multiple Servers Problem (Day 2) ===")
# Beginner realizes: "I need to deploy to 5 servers, not just one!"
# First attempt: More individual variables (gets messy quickly)
server1_name = "web-01"
server1_ip = "192.168.1.10"
server2_name = "web-02"  
server2_ip = "192.168.1.11"
# ... this gets crazy with more servers!

# Beginner learns about lists
server_names = ["web-01", "web-02", "web-03"]
server_ips = ["192.168.1.10", "192.168.1.11", "192.168.1.12"]

def deploy_simple(name):
    print(f"Deploying to {name}")

# Problem: Have to manage multiple lists, easy to get out of sync
for server in server_names:
    deploy_simple(server)

print("\n=== Step 3: Discovering Tuples (Day 3) ===")
# Beginner learns: "I can keep related data together!"
servers = [
    ("web-01", "192.168.1.10", 80),    # name, ip, port
    ("web-02", "192.168.1.11", 80),    # name, ip, port  
    ("api-01", "192.168.1.20", 8080)   # name, ip, port
]

# First tuple experiment - test with one server
print("Testing with first server:")
first_server = servers[0]  # Get first tuple
print(f"First server tuple: {first_server}")

# Beginner manually unpacks to understand
name, ip, port = first_server
print(f"Unpacked: name={name}, ip={ip}, port={port}")
deploy_to_server(name, ip, port)

print("\n=== Step 4: Scaling Up (Day 4) ===")
# Confident enough to loop through all servers
print("Deploying to all servers:")
for name, ip, port in servers:  # Unpack each tuple
    deploy_to_server(name, ip, port)

print("\n=== Step 5: Real World Complexity (Week 2) ===")
# Beginner discovers different server types need different handling
servers_detailed = [
    ("web-01", "192.168.1.10", 80, "web", "production"),      # name, ip, port, type, env
    ("web-02", "192.168.1.11", 80, "web", "production"),      # name, ip, port, type, env
    ("api-01", "192.168.1.20", 8080, "api", "production"),    # name, ip, port, type, env
    ("cache-01", "192.168.1.30", 6379, "redis", "production") # name, ip, port, type, env
]

def deploy_advanced(name, ip, port, server_type, environment):
    print(f"Deploying {server_type} server {name} to {environment} at {ip}:{port}")

# Testing different approaches
print("Method 1: Direct unpacking in loop")
for name, ip, port, server_type, env in servers_detailed:
    deploy_advanced(name, ip, port, server_type, env)

print("\nMethod 2: Conditional deployment based on server type")
for name, ip, port, server_type, env in servers_detailed:
    if server_type == "web":
        print(f"Special web server deployment for {name}")
        deploy_advanced(name, ip, port, server_type, env)
    elif server_type == "redis":
        print(f"Redis requires special configuration for {name}")
        deploy_advanced(name, ip, port, server_type, env)
    else:
        deploy_advanced(name, ip, port, server_type, env)

print("\n=== Step 6: Function Parameter Order Problems (Week 3) ===")
# Beginner discovers order matters when integrating with existing functions

# Existing monitoring function (different parameter order!)
def monitor_server(environment, server_type, name, ip):  # Different order!
    print(f"Monitoring {environment} {server_type} server {name} at {ip}")

# WRONG: Direct unpacking doesn't match function order
print("Attempting direct unpacking (will be wrong):")
for name, ip, port, server_type, env in servers_detailed:
    # This would be wrong: monitor_server(name, ip, port, server_type, env)
    # Function expects: (environment, server_type, name, ip)
    
    # CORRECT: Reorder variables to match function
    monitor_server(env, server_type, name, ip)  # Reorder to match function parameters

print("\n=== Step 7: Error Debugging (Week 4) ===")
# Beginner makes common mistakes and learns to debug

# Common mistake: Wrong number of variables
problematic_data = [
    ("web-01", "192.168.1.10"),  # Only 2 items, but function expects 5
    ("api-01", "192.168.1.20", 8080, "api")  # Only 4 items, but function expects 5
]

print("Debugging unpacking errors:")
for server_data in problematic_data:
    print(f"Server data: {server_data} (length: {len(server_data)})")
    
    # Beginner learns to handle different data structures
    if len(server_data) == 2:
        name, ip = server_data
        print(f"Simple server: {name} at {ip}")
    elif len(server_data) == 4:
        name, ip, port, server_type = server_data
        print(f"Partial server: {name} ({server_type}) at {ip}:{port}")
    else:
        print("Unknown server data format")
```

### **Example 2: Advanced Tuple Workflow - DevOps Configuration Management**

```python
# === ADVANCED TUPLE WORKFLOW: DEVOPS CONFIGURATION MANAGEMENT ===

print("=== Advanced DevOps Tuple Management ===")

# Step 1: Define multiple configuration sources with different tuple structures
print("Step 1: Defining different configuration sources")

# Production servers (name, ip, port, cpu_cores, memory_gb)
production_servers = [
    ("web-prod-01", "10.0.1.10", 80, 4, 8),
    ("web-prod-02", "10.0.1.11", 80, 4, 8),
    ("db-prod-01", "10.0.1.20", 5432, 8, 32)
]

# Monitoring endpoints (service_name, endpoint, port, check_interval, timeout)
monitoring_configs = [
    ("web-health", "/health", 80, 30, 5),
    ("api-status", "/status", 8080, 60, 10),
    ("db-health", "/metrics", 5432, 120, 15)
]

# Backup configurations (source_path, destination, frequency, retention_days)
backup_configs = [
    ("/var/www", "s3://backups/web", "daily", 30),
    ("/var/lib/postgresql", "s3://backups/db", "hourly", 7),
    ("/etc/nginx", "s3://backups/config", "weekly", 90)
]

# Step 2: Create specialized functions for each configuration type
print("\nStep 2: Creating specialized functions")

def provision_server(name, ip, port, cpu_cores, memory_gb):
    print(f"Provisioning {name}: {cpu_cores} cores, {memory_gb}GB RAM at {ip}:{port}")

def setup_monitoring(service, endpoint, port, interval, timeout):
    print(f"Monitoring {service}{endpoint}:{port} every {interval}s (timeout: {timeout}s)")

def schedule_backup(source, destination, frequency, retention):
    print(f"Backup {source} → {destination} ({frequency}, keep {retention} days)")

# Step 3: Process each configuration type separately
print("\nStep 3: Processing different configuration types")

print("Provisioning production servers:")
for name, ip, port, cores, memory in production_servers:  # Unpack server tuple
    provision_server(name, ip, port, cores, memory)

print("\nSetting up monitoring:")
for service, endpoint, port, interval, timeout in monitoring_configs:  # Unpack monitoring tuple
    setup_monitoring(service, endpoint, port, interval, timeout)

print("\nScheduling backups:")
for source, dest, freq, retention in backup_configs:  # Unpack backup tuple
    schedule_backup(source, dest, freq, retention)

# Step 4: Advanced integration - combining different tuple sources
print("\nStep 4: Advanced integration across configuration types")

def deploy_complete_environment():
    print("=== Complete Environment Deployment ===")
    
    # Deploy servers first
    for name, ip, port, cores, memory in production_servers:
        provision_server(name, ip, port, cores, memory)
        
        # Find matching monitoring config for this server
        for service, endpoint, mon_port, interval, timeout in monitoring_configs:
            if "web" in name and "web" in service:
                setup_monitoring(service, endpoint, mon_port, interval, timeout)
            elif "db" in name and "db" in service:
                setup_monitoring(service, endpoint, mon_port, interval, timeout)
        
        # Setup backups based on server type
        for source, dest, freq, retention in backup_configs:
            if "web" in name and "www" in source:
                schedule_backup(source, dest, freq, retention)
            elif "db" in name and "postgresql" in source:
                schedule_backup(source, dest, freq, retention)

deploy_complete_environment()

# Step 5: Error handling and validation
print("\nStep 5: Error handling and validation")

def validate_and_deploy(server_tuple):
    """Validate server configuration before deployment"""
    try:
        name, ip, port, cores, memory = server_tuple  # Attempt to unpack
        
        # Validation logic
        if not name or not ip:
            print(f"ERROR: Invalid server config {server_tuple} - missing name or IP")
            return False
            
        if cores < 1 or memory < 1:
            print(f"ERROR: Invalid resources for {name} - cores: {cores}, memory: {memory}")
            return False
            
        if port < 1 or port > 65535:
            print(f"ERROR: Invalid port {port} for {name}")
            return False
            
        print(f"✓ Valid configuration for {name}")
        provision_server(name, ip, port, cores, memory)
        return True
        
    except ValueError as e:
        print(f"ERROR: Cannot unpack server tuple {server_tuple} - {e}")
        return False

# Test with various configurations including invalid ones
test_configs = [
    ("web-test-01", "10.0.1.100", 80, 2, 4),  # Valid
    ("", "10.0.1.101", 80, 2, 4),              # Invalid - no name
    ("api-test-01", "10.0.1.102", 70000, 2, 4), # Invalid - port too high
    ("db-test-01", "10.0.1.103"),              # Invalid - missing values
]

print("Validating server configurations:")
for config in test_configs:
    validate_and_deploy(config)

# Step 6: Dynamic tuple handling based on environment
print("\nStep 6: Environment-specific tuple handling")

def get_environment_config(env_name):
    """Return different tuple structures based on environment"""
    if env_name == "development":
        # Development: (name, ip, port) - minimal config
        return [
            ("dev-web", "127.0.0.1", 8000),
            ("dev-api", "127.0.0.1", 8001)
        ]
    elif env_name == "staging":
        # Staging: (name, ip, port, replicas) - intermediate config
        return [
            ("staging-web", "10.1.1.10", 80, 2),
            ("staging-api", "10.1.1.11", 8080, 1)
        ]
    else:  # production
        # Production: (name, ip, port, cores, memory) - full config
        return production_servers

def deploy_to_environment(env_name):
    """Deploy with environment-appropriate configuration"""
    print(f"\nDeploying to {env_name} environment:")
    
    configs = get_environment_config(env_name)
    
    for config in configs:
        if env_name == "development":
            name, ip, port = config  # 3-tuple unpacking
            print(f"Dev deployment: {name} at {ip}:{port}")
            
        elif env_name == "staging":
            name, ip, port, replicas = config  # 4-tuple unpacking
            print(f"Staging deployment: {name} at {ip}:{port} ({replicas} replicas)")
            
        else:  # production
            name, ip, port, cores, memory = config  # 5-tuple unpacking
            provision_server(name, ip, port, cores, memory)

# Test different environments
for env in ["development", "staging", "production"]:
    deploy_to_environment(env)

print("\n=== Key Learnings from Advanced Workflow ===")
print("1. Tuple structure must be consistent within each data source")
print("2. Function parameter order must match your unpacking order")
print("3. Different tuple structures require different unpacking patterns")
print("4. Validation prevents errors from malformed tuples")
print("5. Environment-specific handling allows flexible configurations")
print("6. Error handling is crucial when working with external data sources")
``` 