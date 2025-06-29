# Loops and Terminology Q&A

**1. What do for loops use?**

For loops use **iterables**. An iterable is something you can loop through like lists, strings, or ranges.

```python
servers = ["web-01", "db-01", "cache-01"]
for server in servers:  # servers is the iterable
    print(server)
```

**2. What are parameters vs arguments?**

- **Parameters**: Variables in function definition
- **Arguments**: Actual values passed to function

```python
def check_server(hostname, port):  # hostname and port are parameters
    print(f"Checking {hostname}:{port}")

check_server("web-01", 80)  # "web-01" and 80 are arguments
```

**3. Can you nest different loop types?**

Yes. You can put any loop inside any other loop.

```python
# While loop containing a for loop
while system_running:
    for server in servers:
        if check_server(server):
            continue
        else:
            system_running = False
            break
```

**4. What are compound data structures?**

Data structures that contain other data structures.

```python
# Dictionary containing lists
server_config = {
    "web_servers": ["web-01", "web-02"],
    "databases": ["db-01", "db-02"],
    "ports": [80, 443, 3306]
}
```

**5. Can functions be arguments?**

Yes. Functions can be passed as arguments to other functions.

```python
def ping_server(hostname):
    return f"Pinging {hostname}"

def check_all_servers(servers, check_function):
    for server in servers:
        result = check_function(server)
        print(result)

servers = ["web-01", "db-01"]
check_all_servers(servers, ping_server)  # ping_server is the argument
``` 