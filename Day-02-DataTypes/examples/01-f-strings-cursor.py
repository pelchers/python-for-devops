# F-strings Advanced Examples for DevOps

# Basic f-string usage
server_name = "web-server-01"
cpu_usage = 85.7
memory_usage = 72.3

# Simple variable insertion
status_message = f"Server {server_name} is running"
print(status_message)

# Multiple variables with formatting
health_report = f"Server {server_name}: CPU {cpu_usage:.1f}%, Memory {memory_usage:.1f}%"
print(health_report)

# Conditional expressions inside f-strings
alert_status = f"Status: {server_name} - {'ALERT' if cpu_usage > 80 else 'OK'}"
print(alert_status)

# Math expressions
total_usage = f"Total resource usage: {cpu_usage + memory_usage:.1f}%"
print(total_usage)

# Method calls inside f-strings
service_name = "database-service"
formatted_service = f"Service: {service_name.upper()}"
print(formatted_service)

# Multi-line f-string for server report
server_report = f"""
========== SERVER REPORT ==========
Server Name: {server_name}
CPU Usage: {cpu_usage:.1f}%
Memory Usage: {memory_usage:.1f}%
Status: {'CRITICAL' if cpu_usage > 90 else 'WARNING' if cpu_usage > 80 else 'HEALTHY'}
Timestamp: 2023-12-25 10:00:00
===================================
"""
print(server_report)

# Docker command generation with f-strings
image_name = "myapp"
version = "1.2.3"
port = 8080
environment = "production"

docker_cmd = f"docker run -d -p {port}:80 -e ENV={environment} {image_name}:{version}"
print(f"Docker command: {docker_cmd}")

# Log entry formatting
log_level = "ERROR"
timestamp = "2023-12-25 10:15:00"
message = "Database connection failed"

log_entry = f"[{timestamp}] {log_level}: {message} on {server_name}"
print(f"Log entry: {log_entry}") 