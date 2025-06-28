# Advanced String Concepts in Python

## **What is f-string (f"text")?**

**f-strings** (formatted string literals) are the modern, clean way to put variables inside strings.

### **Basic f-string Examples:**

```python
# Old way (hard to read)
name = "web-server-01"
port = 80
message = "Checking " + name + " on port " + str(port)
print(message)  # Output: Checking web-server-01 on port 80

# Modern way with f-strings (clean and readable)
name = "web-server-01"
port = 80
message = f"Checking {name} on port {port}"
print(message)  # Output: Checking web-server-01 on port 80
```

### **f-string Advanced Features:**

```python
# Variables and expressions inside {}
server_name = "database-01"
cpu_usage = 75
memory_usage = 60

# Basic variable insertion
status = f"Server {server_name} status"

# Multiple variables
report = f"Server {server_name}: CPU {cpu_usage}%, Memory {memory_usage}%"

# Expressions inside {}
health = f"CPU status: {cpu_usage}% ({'High' if cpu_usage > 80 else 'Normal'})"

# Math expressions
total_usage = f"Total usage: {cpu_usage + memory_usage}%"

# Method calls
hostname = f"Server: {server_name.upper()}"

# Formatting numbers
price = 1234.567
formatted = f"Price: ${price:.2f}"  # Price: $1234.57
```

**{Without f-strings - Old concatenation way}:**
```python
# Same examples without f-strings (much more verbose and error-prone)
server_name = "database-01"
cpu_usage = 75
memory_usage = 60

# Basic variable insertion
status = "Server " + server_name + " status"
# Output: Server database-01 status

# Multiple variables (need str() for numbers)
report = "Server " + server_name + ": CPU " + str(cpu_usage) + "%, Memory " + str(memory_usage) + "%"
# Output: Server database-01: CPU 75%, Memory 60%

# Expressions (very hard to read)
if cpu_usage > 80:
    cpu_status = "High"
else:
    cpu_status = "Normal"
health = "CPU status: " + str(cpu_usage) + "% (" + cpu_status + ")"
# Output: CPU status: 75% (Normal)

# Math expressions
total_usage = "Total usage: " + str(cpu_usage + memory_usage) + "%"
# Output: Total usage: 135%

# Method calls
hostname = "Server: " + server_name.upper()
# Output: Server: DATABASE-01

# Formatting numbers (manual formatting)
formatted = "Price: $" + "{:.2f}".format(price)  # Or even worse: "Price: $%.2f" % price
# Output: Price: $1234.57
```

---

## **String Formatting Methods Comparison**

### **1. f-strings (Modern - Recommended)**
```python
name = "Alice"
age = 30
score = 95.67

# Clean and readable
message = f"Hello {name}, you are {age} years old with score {score:.1f}"
```

### **2. .format() Method (Older but still used)**
```python
name = "Alice"
age = 30
score = 95.67

# Using .format()
message = "Hello {}, you are {} years old with score {:.1f}".format(name, age, score)

# Named placeholders
message = "Hello {name}, you are {age} years old".format(name=name, age=age)
```

### **3. % Formatting (Oldest - avoid in new code)**
```python
name = "Alice"
age = 30

# Old style % formatting
message = "Hello %s, you are %d years old" % (name, age)
```

---

## **Advanced String Operations**

### **String Methods for DevOps**

```python
# Server log processing
log_line = "  ERROR: Database connection failed on server-01  "

# Cleaning and processing
clean_log = log_line.strip()           # Remove whitespace
log_parts = clean_log.split(":")       # Split by colon
server_name = log_parts[1].split()[-1] # Extract server name

print(f"Server with error: {server_name}")  # server-01

# Case operations
service_name = "WEB-SERVICE-01"
print(f"Service: {service_name.lower()}")     # web-service-01
print(f"Service: {service_name.title()}")     # Web-Service-01

# Checking string content
if "database" in log_line.lower():
    print("Database related error detected")

if log_line.startswith("ERROR"):
    print("This is an error log")

if server_name.endswith("-01"):
    print("This is a primary server")
```

**{Without string methods - Manual processing}:**
```python
# Same log processing without built-in string methods (much more complex)
log_line = "  ERROR: Database connection failed on server-01  "

# Manual whitespace removal (instead of .strip())
clean_log = log_line
while clean_log.startswith(" ") or clean_log.startswith("\t"):
    clean_log = clean_log[1:]
while clean_log.endswith(" ") or clean_log.endswith("\t"):
    clean_log = clean_log[:-1]

# Manual split by colon (instead of .split(":"))
log_parts = []
current_part = ""
for char in clean_log:
    if char == ":":
        log_parts.append(current_part)
        current_part = ""
    else:
        current_part += char
log_parts.append(current_part)  # Add the last part

# Manual extraction of server name (much more complex)
server_part = log_parts[1]
words = []
current_word = ""
for char in server_part:
    if char == " ":
        if current_word:
            words.append(current_word)
            current_word = ""
    else:
        current_word += char
if current_word:
    words.append(current_word)
server_name = words[-1]  # Get last word

print("Server with error: " + server_name)
# Output: Server with error: server-01

# Manual case operations (instead of .lower(), .title())
service_name = "WEB-SERVICE-01"
lowercase_service = ""
for char in service_name:
    if 'A' <= char <= 'Z':
        lowercase_service += chr(ord(char) + 32)  # Convert to lowercase manually
    else:
        lowercase_service += char

print("Service: " + lowercase_service)
# Output: Service: web-service-01

# Manual string checking (instead of "in" operator and .startswith())
database_found = False
log_lower = ""
for char in log_line:
    if 'A' <= char <= 'Z':
        log_lower += chr(ord(char) + 32)
    else:
        log_lower += char

# Check if "database" is in the string manually
search_term = "database"
for i in range(len(log_lower) - len(search_term) + 1):
    if log_lower[i:i + len(search_term)] == search_term:
        database_found = True
        break

if database_found:
    print("Database related error detected")
# Output: Database related error detected

# Manual startswith check (instead of .startswith())
starts_with_error = True
error_prefix = "ERROR"
if len(clean_log) >= len(error_prefix):
    for i in range(len(error_prefix)):
        if clean_log[i] != error_prefix[i]:
            starts_with_error = False
            break
else:
    starts_with_error = False

if starts_with_error:
    print("This is an error log")
# Output: This is an error log
```

### **String Replacement and Cleaning**

```python
# Configuration file processing
config_template = "server={SERVER_NAME}, port={PORT}, env={ENVIRONMENT}"

# Replace placeholders
production_config = config_template.replace("{SERVER_NAME}", "prod-web-01")
production_config = production_config.replace("{PORT}", "443")
production_config = production_config.replace("{ENVIRONMENT}", "production")

print(production_config)  # server=prod-web-01, port=443, env=production

# Multiple replacements
server_config = "server=localhost,port=8080,debug=true"
updated_config = server_config.replace("localhost", "prod.example.com").replace("8080", "443").replace("true", "false")

# Remove unwanted characters
dirty_hostname = "server-01###"
clean_hostname = dirty_hostname.rstrip("#")  # Remove # from right
clean_hostname = clean_hostname.strip("@#")  # Remove @ and # from both sides
```

**{Without .replace() and .strip() - Manual character processing}:**
```python
# Same replacements without built-in methods (much more error-prone)
config_template = "server={SERVER_NAME}, port={PORT}, env={ENVIRONMENT}"

# Manual replacement (instead of .replace())
def manual_replace(text, old, new):
    result = ""
    i = 0
    while i < len(text):
        if i <= len(text) - len(old) and text[i:i+len(old)] == old:
            result += new
            i += len(old)
        else:
            result += text[i]
            i += 1
    return result

# Multiple manual replacements
production_config = manual_replace(config_template, "{SERVER_NAME}", "prod-web-01")
production_config = manual_replace(production_config, "{PORT}", "443")
production_config = manual_replace(production_config, "{ENVIRONMENT}", "production")

print(production_config)
# Output: server=prod-web-01, port=443, env=production

# Manual multiple replacements
server_config = "server=localhost,port=8080,debug=true"
updated_config = manual_replace(server_config, "localhost", "prod.example.com")
updated_config = manual_replace(updated_config, "8080", "443")
updated_config = manual_replace(updated_config, "true", "false")
# Output: server=prod.example.com,port=443,debug=false

# Manual character removal (instead of .rstrip() and .strip())
dirty_hostname = "server-01###"

# Remove # from right (manual .rstrip())
clean_hostname = dirty_hostname
while clean_hostname and clean_hostname[-1] == "#":
    clean_hostname = clean_hostname[:-1]

# Remove @ and # from both sides (manual .strip())
unwanted_chars = "@#"
while clean_hostname and clean_hostname[0] in unwanted_chars:
    clean_hostname = clean_hostname[1:]
while clean_hostname and clean_hostname[-1] in unwanted_chars:
    clean_hostname = clean_hostname[:-1]
# Final result: "server-01"
```

---

## **Multi-line Strings and Templates**

### **Triple Quotes for Multi-line Strings**

```python
# Configuration file template
nginx_config = """
server {
    listen 80;
    server_name example.com;
    
    location / {
        proxy_pass http://localhost:8080;
        proxy_set_header Host $host;
    }
}
"""

# SQL query template
database_query = """
SELECT server_name, cpu_usage, memory_usage 
FROM server_stats 
WHERE environment = 'production' 
  AND cpu_usage > 80
ORDER BY cpu_usage DESC;
"""

# Multi-line f-string
server_name = "web-01"
cpu = 85
memory = 70

server_report = f"""
Server Status Report
====================
Server: {server_name}
CPU Usage: {cpu}%
Memory Usage: {memory}%
Status: {'ALERT' if cpu > 80 or memory > 80 else 'OK'}
"""
print(server_report)
```

**{Without triple quotes and f-strings - Manual concatenation}:**
```python
# Same multi-line report without triple quotes (much more verbose)
server_name = "web-01"
cpu = 85
memory = 70

# Manual string building with \n for line breaks
status = "ALERT" if cpu > 80 or memory > 80 else "OK"
server_report = "\n" + \
                "Server Status Report\n" + \
                "====================\n" + \
                "Server: " + server_name + "\n" + \
                "CPU Usage: " + str(cpu) + "%\n" + \
                "Memory Usage: " + str(memory) + "%\n" + \
                "Status: " + status + "\n"

print(server_report)
# Output: Multi-line server status report with ALERT status

# Alternative using list and join (slightly better but still verbose)
report_lines = [
    "",
    "Server Status Report",
    "====================",
    "Server: " + server_name,
    "CPU Usage: " + str(cpu) + "%",
    "Memory Usage: " + str(memory) + "%",
    "Status: " + status,
    ""
]
server_report = "\n".join(report_lines)
print(server_report)
# Output: Same formatted report as above
```

### **Template Strings for Configuration**

```python
from string import Template

# Template for server configuration
server_template = Template("""
[server]
hostname = $hostname
port = $port
environment = $env
ssl_enabled = $ssl

[monitoring]
cpu_threshold = $cpu_limit
memory_threshold = $memory_limit
""")

# Generate different environment configs
dev_config = server_template.substitute(
    hostname="dev.example.com",
    port="8080",
    env="development", 
    ssl="false",
    cpu_limit="90",
    memory_limit="85"
)

prod_config = server_template.substitute(
    hostname="prod.example.com",
    port="443",
    env="production",
    ssl="true", 
    cpu_limit="80",
    memory_limit="75"
)

print("Development Config:")
print(dev_config)
print("\nProduction Config:")
print(prod_config)
```

**{Without Template class - Manual placeholder replacement}:**
```python
# Same template functionality without Template class (more error-prone)
config_template = """
[server]
hostname = $hostname
port = $port
environment = $env
ssl_enabled = $ssl

[monitoring]
cpu_threshold = $cpu_limit
memory_threshold = $memory_limit
"""

# Manual replacement function (like we did earlier but more complex)
def manual_template_substitute(template, **kwargs):
    result = template
    for key, value in kwargs.items():
        placeholder = "$" + key
        # Manual replacement without .replace()
        new_result = ""
        i = 0
        while i < len(result):
            if i <= len(result) - len(placeholder) and result[i:i+len(placeholder)] == placeholder:
                new_result += str(value)
                i += len(placeholder)
            else:
                new_result += result[i]
                i += 1
        result = new_result
    return result
# This function manually replaces all $placeholders with actual values

# Generate configs manually
dev_config = manual_template_substitute(
    config_template,
    hostname="dev.example.com",
    port="8080",
    env="development",
    ssl="false",
    cpu_limit="90",
    memory_limit="85"
)

prod_config = manual_template_substitute(
    config_template,
    hostname="prod.example.com",
    port="443",
    env="production",
    ssl="true",
    cpu_limit="80",
    memory_limit="75"
)

print("Development Config (manual):")
print(dev_config)
# Output: Complete dev config with replaced values
print("\nProduction Config (manual):")
print(prod_config)
# Output: Complete prod config with replaced values
```

---

## **String Validation and Parsing**

### **Checking String Properties**

```python
# Server name validation
def validate_server_name(name):
    """Validate server name format"""
    if not name:
        return False, "Server name cannot be empty"
    
    if not name.replace("-", "").replace("_", "").isalnum():
        return False, "Server name can only contain letters, numbers, hyphens, and underscores"
    
    if len(name) > 50:
        return False, "Server name too long (max 50 characters)"
    
    if name.startswith("-") or name.endswith("-"):
        return False, "Server name cannot start or end with hyphen"
    
    return True, "Valid server name"

# Test server names
test_names = ["web-server-01", "db_server", "invalid@server", "", "-bad-start", "good-server"]

for name in test_names:
    is_valid, message = validate_server_name(name)
    print(f"'{name}': {message}")
```

**{Without string methods - Manual character validation}:**
```python
# Same validation without string methods (much more complex and error-prone)
def validate_server_name_manual(name):
    """Validate server name format manually"""
    # Check if empty (without 'not name')
    if len(name) == 0:
        return False, "Server name cannot be empty"
    
    # Manual character validation (without .replace() and .isalnum())
    valid_chars_only = True
    for char in name:
        # Check if char is alphanumeric, hyphen, or underscore manually
        is_letter = ('a' <= char <= 'z') or ('A' <= char <= 'Z')
        is_digit = ('0' <= char <= '9')
        is_hyphen = (char == '-')
        is_underscore = (char == '_')
        
        if not (is_letter or is_digit or is_hyphen or is_underscore):
            valid_chars_only = False
            break
    
    if not valid_chars_only:
        return False, "Server name can only contain letters, numbers, hyphens, and underscores"
    
    # Manual length check (without len())
    char_count = 0
    for char in name:
        char_count += 1
    if char_count > 50:
        return False, "Server name too long (max 50 characters)"
    
    # Manual startswith/endswith check (without .startswith() and .endswith())
    if name[0] == "-" or name[char_count - 1] == "-":
        return False, "Server name cannot start or end with hyphen"
    
    return True, "Valid server name"

# Test with manual validation
test_names = ["web-server-01", "db_server", "invalid@server", "", "-bad-start", "good-server"]

for name in test_names:
    try:
        is_valid, message = validate_server_name_manual(name)
        print("'" + name + "': " + message)  # Manual concatenation instead of f-string
    except IndexError:  # Handle empty string case for manual indexing
        print("'" + name + "': Server name cannot be empty")
# Output: Validation results for each test name (same as modern version)
```

### **Parsing Log Files and Data**

```python
# Parse different log formats
def parse_apache_log(log_line):
    """Parse Apache access log format"""
    # Example: 192.168.1.1 - - [25/Dec/2023:10:00:00 +0000] "GET /index.html HTTP/1.1" 200 1234
    parts = log_line.split()
    
    if len(parts) >= 10:
        ip_address = parts[0]
        timestamp = parts[3].strip('[') + " " + parts[4].strip(']')
        method = parts[5].strip('"')
        url = parts[6]
        status_code = parts[8]
        response_size = parts[9]
        
        return {
            'ip': ip_address,
            'timestamp': timestamp,
            'method': method,
            'url': url,
            'status': status_code,
            'size': response_size
        }
    return None

# Parse CSV-like server stats
def parse_server_stats(stats_line):
    """Parse comma-separated server stats"""
    # Example: "web-01,85,70,active,2023-12-25 10:00:00"
    parts = [part.strip() for part in stats_line.split(',')]
    
    if len(parts) == 5:
        return {
            'server': parts[0],
            'cpu': int(parts[1]),
            'memory': int(parts[2]),
            'status': parts[3],
            'timestamp': parts[4]
        }
    return None

# Test parsing
log_sample = '192.168.1.1 - - [25/Dec/2023:10:00:00 +0000] "GET /index.html HTTP/1.1" 200 1234'
stats_sample = "web-01, 85, 70, active, 2023-12-25 10:00:00"

parsed_log = parse_apache_log(log_sample)
parsed_stats = parse_server_stats(stats_sample)

print(f"Parsed log: {parsed_log}")
print(f"Parsed stats: {parsed_stats}")
```

---

## **Performance and Best Practices**

### **Efficient String Building**

```python
# BAD: Concatenating in a loop (slow for large data)
servers = ["web-01", "web-02", "db-01", "cache-01"]
report = ""
for server in servers:
    report += f"Server: {server}\n"  # Creates new string each time

# GOOD: Using join() for multiple concatenations
servers = ["web-01", "web-02", "db-01", "cache-01"]
server_lines = [f"Server: {server}" for server in servers]
report = "\n".join(server_lines)

# GOOD: Using list and join for complex building
report_lines = []
for server in servers:
    status = "active"  # Would be actual check
    report_lines.append(f"Server: {server} - Status: {status}")
final_report = "\n".join(report_lines)
```

**{Without .join() - Only concatenation available (very slow for large data)}:**
```python
# Same building without .join() - demonstrating why it's slow
servers = ["web-01", "web-02", "db-01", "cache-01"]

# This is what you'd have to do without .join() - much slower
# Each += creates a completely new string in memory
report = ""
for server in servers:
    # Without f-strings AND without .join() - worst case scenario
    report = report + "Server: " + server + "\n"
# Output: Server list with newlines (slow performance)

# For complex building without .join() - very inefficient
final_report = ""
for server in servers:
    status = "active"  # Would be actual check
    # Each concatenation creates a new string object in memory
    final_report = final_report + "Server: " + server + " - Status: " + status + "\n"
# Output: Server list with status (very slow for large lists)

# Why this is bad:
# - For 4 servers: 4 string creations
# - For 100 servers: 100 string creations  
# - For 10,000 servers: 10,000 string creations (very slow!)
# 
# .join() reads all pieces once and creates ONE final string
# += concatenation creates a new string for EVERY addition
```

### **String Formatting Best Practices**

```python
# Use f-strings for most cases (Python 3.6+)
name = "server-01"
cpu = 85.7

# Good: f-string with formatting
status = f"Server {name} CPU: {cpu:.1f}%"

# Control decimal places
price = 1234.567
formatted = f"${price:.2f}"        # $1234.57
percentage = f"{cpu:.0f}%"         # 86%

# Padding and alignment
servers = ["web-01", "db-primary", "cache"]
for server in servers:
    print(f"Server: {server:<12} Status: OK")  # Left-align with width 12

# Output:
# Server: web-01       Status: OK
# Server: db-primary   Status: OK  
# Server: cache        Status: OK
```

---

## **Common DevOps String Patterns**

### **Environment and Configuration Management**

```python
import os

def generate_docker_command(image, port, env_vars=None):
    """Generate Docker run command with f-strings"""
    base_cmd = f"docker run -d -p {port}:80"
    
    if env_vars:
        env_flags = " ".join([f"-e {key}={value}" for key, value in env_vars.items()])
        base_cmd = f"{base_cmd} {env_flags}"
    
    return f"{base_cmd} {image}"

# Usage
env_variables = {
    "DATABASE_URL": "postgresql://prod-db:5432/app",
    "REDIS_URL": "redis://cache:6379",
    "ENVIRONMENT": "production"
}

docker_cmd = generate_docker_command("myapp:latest", 8080, env_variables)
print(docker_cmd)
```

### **Log Analysis and Reporting**

```python
def analyze_server_logs(log_entries):
    """Analyze server log entries and generate report"""
    error_count = 0
    warning_count = 0
    servers_with_issues = set()
    
    for entry in log_entries:
        if "ERROR" in entry.upper():
            error_count += 1
            # Extract server name from log entry
            if "server-" in entry:
                server = entry.split("server-")[1].split()[0]
                servers_with_issues.add(f"server-{server}")
        elif "WARNING" in entry.upper():
            warning_count += 1
    
    # Generate report with f-strings
    report = f"""
Log Analysis Report
==================
Total Entries Analyzed: {len(log_entries)}
Errors Found: {error_count}
Warnings Found: {warning_count}
Servers with Issues: {', '.join(servers_with_issues) if servers_with_issues else 'None'}

Status: {'CRITICAL' if error_count > 0 else 'WARNING' if warning_count > 0 else 'OK'}
    """.strip()
    
    return report

# Test with sample log entries
sample_logs = [
    "INFO: server-01 started successfully",
    "ERROR: server-02 database connection failed", 
    "WARNING: server-01 high memory usage detected",
    "INFO: server-03 backup completed"
]

analysis = analyze_server_logs(sample_logs)
print(analysis)
```

## **Summary**

### **Key String Concepts for DevOps:**

✅ **f-strings**: Modern, clean way to format strings - `f"Server {name} has {cpu}% CPU"`  
✅ **String methods**: `.strip()`, `.split()`, `.replace()`, `.join()` for data processing  
✅ **Multi-line strings**: Triple quotes for configuration templates  
✅ **String validation**: Check format, length, content for input validation  
✅ **Efficient building**: Use `.join()` for multiple concatenations  
✅ **Template strings**: For configuration file generation  
✅ **Parsing**: Extract data from logs, CSV, and configuration files  

**Remember**: f-strings are the preferred way for string formatting in modern Python! 🚀 