# Advanced String Concepts

**1. f-strings (Formatted String Literals):**

f-strings are the modern way to put variables inside strings.

```python
name = "server-01"
cpu = 75
message = f"Server {name} has {cpu}% CPU usage"
print(message)  # Server server-01 has 75% CPU usage
```

**2. String Methods:**

Built-in functions to manipulate strings.

```python
log = "  ERROR: Connection failed  "
clean_log = log.strip()           # Remove whitespace
parts = clean_log.split(":")      # Split by colon
service = "WEB-SERVICE"
lower_service = service.lower()   # Convert to lowercase
```

**3. Multi-line Strings:**

Use triple quotes for strings spanning multiple lines.

```python
config = """
server_name = web-01
port = 80
ssl_enabled = true
"""
```

**4. String Replacement:**

Replace parts of strings with new values.

```python
template = "Hello {name}, your score is {score}"
message = template.replace("{name}", "Alice").replace("{score}", "95")
```

**5. String Validation:**

Check if strings meet certain criteria.

```python
server_name = "web-server-01"
if server_name.startswith("web"):
    print("This is a web server")

if server_name.endswith("-01"):
    print("This is a primary server")

if "server" in server_name:
    print("Contains 'server'")
```

**6. Efficient String Building:**

Use join() for combining many strings.

```python
# Good way - fast
servers = ["web-01", "web-02", "db-01"]
server_list = ", ".join(servers)

# Bad way - slow for many strings
result = ""
for server in servers:
    result += server + ", "
``` 