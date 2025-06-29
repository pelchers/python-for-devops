# Tuple Row and Column Access - Simple

## Introduction

When working with tuples (especially database records), you use **two numbers** to find data: `[row][column]`

## The Two-Step Pattern

### Step 1: [#] = Which Row (Which Tuple)
### Step 2: [#] = Which Column (Which Value in That Tuple)

```python
# Database records example
users = [
    ("alice", "alice@company.com", "admin", 30),     # Row [0]
    ("bob", "bob@company.com", "user", 25),          # Row [1]  
    ("carol", "carol@company.com", "manager", 35)    # Row [2]
]

# Pattern: users[row][column]
print(users[0][0])  # Row 0, Column 0 = "alice"
print(users[1][2])  # Row 1, Column 2 = "user" 
print(users[2][1])  # Row 2, Column 1 = "carol@company.com"
```

## Visual Guide

```
DATABASE TABLE:
┌─────────┬──────────────────┬─────────┬─────┐
│username │ email            │ role    │ age │
├─────────┼──────────────────┼─────────┼─────┤
│ alice   │ alice@company.com│ admin   │ 30  │  ← Row [0]
│ bob     │ bob@company.com  │ user    │ 25  │  ← Row [1] 
│ carol   │ carol@company.com│ manager │ 35  │  ← Row [2]
└─────────┴──────────────────┴─────────┴─────┘
Column:  [0]      [1]          [2]     [3]

ACCESS PATTERN:
users[0][0] = "alice"                  (Row 0, Column 0)
users[0][1] = "alice@company.com"      (Row 0, Column 1)
users[0][2] = "admin"                  (Row 0, Column 2)
users[0][3] = 30                       (Row 0, Column 3)

users[1][0] = "bob"                    (Row 1, Column 0)
users[1][1] = "bob@company.com"        (Row 1, Column 1)
users[1][2] = "user"                   (Row 1, Column 2)
users[1][3] = 25                       (Row 1, Column 3)
```

## Key Understanding

### First [#] = Row Number (Which Tuple)
- `users[0]` = Get the entire first tuple: `("alice", "alice@company.com", "admin", 30)`
- `users[1]` = Get the entire second tuple: `("bob", "bob@company.com", "user", 25)`
- `users[2]` = Get the entire third tuple: `("carol", "carol@company.com", "manager", 35)`

### Second [#] = Column Number (Which Value)
- `users[0][0]` = From first tuple, get first value: `"alice"`
- `users[0][1]` = From first tuple, get second value: `"alice@company.com"`
- `users[0][2]` = From first tuple, get third value: `"admin"`
- `users[0][3]` = From first tuple, get fourth value: `30`

## Real Examples

```python
# Server data from database
servers = [
    ("web-01", "192.168.1.10", 80, "active"),      # Row [0]
    ("web-02", "192.168.1.11", 80, "maintenance"), # Row [1]
    ("db-01", "192.168.1.20", 5432, "active")      # Row [2]
]

# Get specific server info
first_server_name = servers[0][0]    # "web-01"
first_server_ip = servers[0][1]      # "192.168.1.10"
first_server_port = servers[0][2]    # 80
first_server_status = servers[0][3]  # "active"

# Get different server info
second_server_name = servers[1][0]   # "web-02"
second_server_status = servers[1][3] # "maintenance"

# Get third server info
third_server_name = servers[2][0]    # "db-01"
third_server_port = servers[2][2]    # 5432
```

## Step-by-Step Process

### Example: Get Bob's email address

```python
users = [
    ("alice", "alice@company.com", "admin", 30),     # Row [0]
    ("bob", "bob@company.com", "user", 25),          # Row [1]  
    ("carol", "carol@company.com", "manager", 35)    # Row [2]
]

# Step 1: Find Bob's row = Row [1]
# Step 2: Find email column = Column [1]
# Answer: users[1][1]

bob_email = users[1][1]  # "bob@company.com"
```

### Example: Get Carol's role

```python
# Step 1: Find Carol's row = Row [2]
# Step 2: Find role column = Column [2] 
# Answer: users[2][2]

carol_role = users[2][2]  # "manager"
```

## Common Patterns

### Get All Data for One Person (Row)
```python
# Get all of Alice's data
alice_data = users[0]  # ("alice", "alice@company.com", "admin", 30)

# Get all of Bob's data
bob_data = users[1]    # ("bob", "bob@company.com", "user", 25)
```

### Get Same Column from Different Rows
```python
# Get all usernames (column 0 from all rows)
alice_name = users[0][0]  # "alice"
bob_name = users[1][0]    # "bob" 
carol_name = users[2][0]  # "carol"

# Get all ages (column 3 from all rows)
alice_age = users[0][3]   # 30
bob_age = users[1][3]     # 25
carol_age = users[2][3]   # 35
```

## Modification (Convert to List First)

```python
# ❌ Cannot modify tuples directly
# users[0][2] = "superadmin"  # ERROR!

# ✅ Convert to list first
user_list = list(users[0])  # Convert Alice's tuple to list
user_list[2] = "superadmin" # Now you can change the role
print(user_list)            # ["alice", "alice@company.com", "superadmin", 30]
```

## Database Examples

```python
# Typical database query result
cursor.execute("SELECT username, email, role, age FROM users")
database_results = cursor.fetchall()

# Results look like:
# [
#   ("alice", "alice@company.com", "admin", 30),
#   ("bob", "bob@company.com", "user", 25),
#   ("carol", "carol@company.com", "manager", 35)
# ]

# Access pattern: database_results[row][column]
first_user_name = database_results[0][0]    # "alice"
second_user_email = database_results[1][1]  # "bob@company.com"
third_user_role = database_results[2][2]    # "manager"
```

## Remember

- **First [#]** = Which row (which tuple)
- **Second [#]** = Which column (which value in that tuple)
- **Pattern**: `data[row][column]`
- **Tuples cannot be changed** - convert to list if you need to modify
- **Database records** typically come as tuples
- **Each row** is one complete record (tuple)
- **Each column** is one piece of data within that record 