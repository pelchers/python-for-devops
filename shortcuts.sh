#!/bin/bash
# Quick navigation shortcuts for python-for-devops project

# Function to go to assignment directory
assignment() {
    cd "$(dirname "$0")/Day-06/02-Assignment/01-Questions"
}

# Function to run assignment
run-assignment() {
    assignment
    python assignment.py
}

# Function to edit assignment  
edit-assignment() {
    assignment
    code assignment.py  # Opens in VS Code
}

echo "Shortcuts loaded! Use: assignment, run-assignment, edit-assignment" 