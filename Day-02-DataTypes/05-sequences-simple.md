# Sequence Types - Simple

## Introduction

Sequence types are ordered collections of items. Python has three main sequence types.

## The Three Sequence Types

### 1. Strings (str) - Text Sequences
```python
text = "Hello, World"
server_name = "web-server-01"
```

### 2. Lists (list) - Mutable Sequences  
```python
servers = ["web-01", "web-02", "db-01"]
numbers = [1, 2, 3, 4, 5]
```

### 3. Tuples (tuple) - Immutable Sequences
```python
coordinates = (10, 20)
server_config = ("192.168.1.10", 80, "production")
```

## Mutable vs Immutable

### Mutable = Can Be Changed After Creation
### Immutable = Cannot Be Changed After Creation

**Lists are Mutable (Can Change):**
```python
my_list = [1, 2, 3]
print(my_list)         # [1, 2, 3]

my_list[0] = 10        # Change first item
print(my_list)         # [10, 2, 3]

my_list.append(4)      # Add new item
print(my_list)         # [10, 2, 3, 4]
```

**Tuples are Immutable (Cannot Change):**
```python
my_tuple = (1, 2, 3)
print(my_tuple)        # (1, 2, 3)

# my_tuple[0] = 10     # ERROR! Cannot change
# my_tuple.append(4)   # ERROR! Cannot add
```

**Strings are Immutable (Cannot Change):**
```python
text = "Hello"
print(text)            # Hello

# text[0] = "h"        # ERROR! Cannot change individual characters
```

## Indexing - Accessing Items by Position

All sequences use **index positions** starting from **0**:

```python
my_list = ["apple", "banana", "cherry"]
#           ↑        ↑         ↑
#         [0]      [1]       [2]

print(my_list[0])      # apple (first item)
print(my_list[1])      # banana (second item)
print(my_list[2])      # cherry (third item)
```

**Same for tuples:**
```python
coordinates = (100, 200, 300)
print(coordinates[0])  # 100
print(coordinates[1])  # 200
print(coordinates[2])  # 300
```

**Same for strings:**
```python
word = "Python"
print(word[0])         # P
print(word[1])         # y
print(word[2])         # t
```

## When to Use Each Type

**Use Lists when:**
- Data will change (add/remove items)
- Building collections dynamically
- Need flexibility

```python
# Server inventory that changes
active_servers = ["web-01", "web-02"]
active_servers.append("web-03")    # Add new server
active_servers.remove("web-01")    # Remove server
```

**Use Tuples when:**
- Data is fixed/permanent
- Representing coordinates or configurations
- Want to prevent accidental changes

```python
# Server config that should not change
server_config = ("192.168.1.10", 80, "production")
# Cannot accidentally modify this config
```

**Use Strings when:**
- Working with text
- Server names, messages, file paths

```python
# Text data
server_name = "database-01"
log_message = "Connection successful"
file_path = "/var/log/nginx/access.log"
```

## Key Differences Summary

| **Feature** | **List** | **Tuple** | **String** |
|-------------|----------|-----------|------------|
| **Mutable?** | ✅ Yes | ❌ No | ❌ No |
| **Syntax** | `[1, 2, 3]` | `(1, 2, 3)` | `"Hello"` |
| **Can add items?** | ✅ Yes | ❌ No | ❌ No |
| **Can change items?** | ✅ Yes | ❌ No | ❌ No |
| **Indexing** | `list[0]` | `tuple[0]` | `string[0]` |

## Real-World Examples

**Server Management:**
```python
# Dynamic server list (use list)
web_servers = ["web-01", "web-02"]
web_servers.append("web-03")      # Add new server

# Fixed server config (use tuple)  
db_config = ("db.example.com", 5432, "postgres")

# Server names (use strings)
primary_server = "web-primary-01"
backup_server = "web-backup-01"
```

**Data Processing:**
```python
# Process server data
servers = ["web-01", "web-02", "db-01"]

# Access each server by index
print(f"First server: {servers[0]}")    # web-01
print(f"Second server: {servers[1]}")   # web-02
print(f"Third server: {servers[2]}")    # db-01

# Loop through all servers
for server in servers:
    print(f"Processing {server}")
```

## Remember

- **Lists** = Flexible, can change (`[]`)
- **Tuples** = Fixed, cannot change (`()`)  
- **Strings** = Text, cannot change (`""`)
- **Indexing** = Start counting from 0: `[0]`, `[1]`, `[2]`
- **Choose based on your needs** - changing data vs fixed data 